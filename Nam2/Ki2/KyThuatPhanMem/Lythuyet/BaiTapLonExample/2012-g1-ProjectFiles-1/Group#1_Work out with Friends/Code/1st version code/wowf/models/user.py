from __future__ import unicode_literals
import hashlib
import os
from sqlalchemy.orm import synonym
from sqlalchemy.schema import Column
from sqlalchemy.sql import and_, or_, func
from sqlalchemy.types import (
    Boolean, CHAR, Date, DateTime, Enum, Integer, Numeric,
    Unicode)
from wowf.config import settings
from wowf.lib.image import StoredImage, upload_and_make_thumbnails
from wowf.lib.pagination import Pager
from wowf.lib.utils import calculate_bmi, current_timestamp, years_ago
from wowf.models.meta import Base, DBSession


# BMI category ranges
UNDER = 18.5
NORMAL = (18.5, 24.9)
OVER = (25.0, 29.9)
OBESE = 30.0


class User(Base):

    __tablename__ = 'users'
    index_fields = ['username']
    id = Column(Integer(unsigned=True), primary_key=True)
    username = Column(Unicode(10), nullable=False, unique=True)
    email = Column(Unicode(254), nullable=False, unique=True)
    _password = Column('password', CHAR(60), nullable=False)
    gender = Column(Enum('F', 'M', name='user_genders'), nullable=False)
    dob = Column(Date, nullable=False)
    weight = Column(Numeric(7, 4), nullable=False, doc='weight in kilograms')
    height = Column(Numeric(5, 4), nullable=False, doc='height in meters')
    timezone = Column(Unicode(50))
    _avatar = Column('avatar', Unicode(40))
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, nullable=False, default=current_timestamp)
    last_active_at = Column(DateTime, nullable=False, default=current_timestamp)

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        '''
        Hash the given password.
        '''
        from wowf.lib.auth import Auth
        self._password = Auth.hash_password(password)

    password = synonym('_password', descriptor=property(_get_password, _set_password))

    def _get_avatar(self):
        '''
        Return a stored image, to allow different versions of the avatar to be
        served.

        e.g: `user.avatar.large` would return the large version, while
        `user.avatar` would return the original.
        '''
        avatar = self._avatar
        versions = settings.from_prefix('avatar_size_')
        if not avatar:
            avatar = settings.avatar_default
        return StoredImage(settings.avatar_dir, avatar, versions)

    def _set_avatar(self, avatar):
        '''
        Upload the avatar and set the necessary reference to it.
        '''
        filename = '%s%s' % (hashlib.md5(str(self.id)).hexdigest(),
                             os.path.splitext(avatar.filename)[1])
        versions = settings.from_prefix('avatar_size_')
        upload_and_make_thumbnails(avatar.file, settings.avatar_dir, filename, versions)
        self._avatar = filename

    avatar = synonym('_avatar', descriptor=property(_get_avatar, _set_avatar))

    @property
    def age(self):
        '''
        Calculate this users age.
        '''
        return years_ago(self.dob)

    @property
    def bmi(self):
        '''
        Calculate this users Body Mass Index, which is a useful indicator of
        health.
        '''
        return calculate_bmi(self.weight, self.height)

    @property
    def bmi_category(self):
        '''
        Return the category this user belongs to based on BMI.
        '''
        bmi = self.bmi
        if bmi < UNDER:
            return 'under weight'
        elif NORMAL[0] <= bmi <= NORMAL[1]:
            return 'normal weight'
        elif OVER[0] <= bmi <= OVER[1]:
            return 'over weight'
        elif bmi >= OBESE:
            return'obese'

    @property
    def total_points(self):
        '''
        Calculate how many points this user has in total.
        '''
        points = (DBSession.query(func.sum(Workout.points))
                  .filter(Workout.user_id==self.id)
                  .scalar())
        return int(points or 0)

    def __init__(self, username, email, password, gender, dob, weight, height):
        self.username = username
        self.email = email
        self.password = password
        self.gender = gender
        self.dob = dob
        self.weight = weight
        self.height = height

    def __unicode__(self):
        return self.username

    @classmethod
    def get_by_username(cls, username):
        '''
        Search by username.
        '''
        return cls.query.filter(cls.username==username).first()

    @classmethod
    def get_by_email(cls, email):
        '''
        Search by email.
        '''
        return cls.query.filter(cls.email==email).first()

    @classmethod
    def create(cls, username, email, password, gender, dob, weight, height):
        return super(User, cls).create(
            username=username, email=email, password=password, gender=gender,
            dob=dob, weight=weight, height=height)

    @classmethod
    def search(cls, terms, limit=50, page=1):
        '''
        Perform a fulltext search, matching the given terms.
        '''
        pager = Pager(page, limit)
        return (cls._get_search_query(terms)
                .order_by(cls.username.asc())
                .limit(pager.limit)
                .offset(pager.offset)
                .all())

    @classmethod
    def count_search_results(cls, terms):
        return cls._get_search_query(terms).count()

    def is_user(self, user):
        '''
        Quick and easy test to check if the given user is this user.

        Some templating engines don't allow the use of `is` in conditionals.
        '''
        return user is self

    def update_profile(self, username, email, gender, dob, weight, height, timezone):
        '''
        Update this users profile, with both required and optional data.
        '''
        self.username = username
        self.email = email
        self.gender = gender
        self.dob = dob
        self.weight = weight
        self.height = height
        self.timezone = timezone or None

    def update_password(self, password):
        '''
        Update this users password.
        '''
        self.password = password

    def update_avatar(self, avatar):
        '''
        Update this users avatar (profile pic)
        '''
        self.avatar = avatar

    def get_average_speed(self, distance):
        '''
        Calculate the average speed (speed challenge) for a given distance.
        '''
        speed = (DBSession.query(func.avg(SpeedWorkout.speed))
                 .outerjoin(SpeedChallenge, SpeedChallenge.id==SpeedWorkout.challenge_id)
                 .filter(SpeedChallenge.distance==distance)
                 .filter(SpeedWorkout.user_id==self.id)
                 .scalar())
        return speed

    def get_average_heart_rate(self, duration):
        '''
        Calculate the average heart rate (endurance challenge) for a given
        duration.
        '''
        heart_rate = (DBSession.query(func.avg(EnduranceWorkout.heart_rate))
                      .outerjoin(EnduranceChallenge, EnduranceChallenge.id==EnduranceWorkout.challenge_id)
                      .filter(EnduranceChallenge.duration==duration)
                      .filter(EnduranceWorkout.user_id==self.id)
                      .scalar())
        return heart_rate

    def get_average_calories_burned(self, duration):
        '''
        Calculate the average calories burned (endurance challenge) for a given
        duration.
        '''
        calories_burned = (DBSession.query(func.avg(EnduranceWorkout.calories_burned))
                           .outerjoin(EnduranceChallenge, EnduranceChallenge.id==EnduranceWorkout.challenge_id)
                           .filter(EnduranceChallenge.duration==duration)
                           .filter(EnduranceWorkout.user_id==self.id)
                           .scalar())
        return calories_burned

    def get_average_bench_press_repetitions(self, percentage):
        '''
        Calculate the average bench press repetitions (bench press challenge)
        for a given percentage.
        '''
        repetitions = (DBSession.query(func.avg(BenchPressWorkout.repetitions))
                       .outerjoin(BenchPressChallenge, BenchPressChallenge.id==BenchPressWorkout.challenge_id)
                       .filter(BenchPressChallenge.percentage==percentage)
                       .filter(BenchPressWorkout.user_id==self.id)
                       .scalar())
        return repetitions

    def get_average_squat_repetitions(self, percentage):
        '''
        Calculate the average squat repetitions (squat challenge) for a given
        percentage.
        '''
        repetitions = (DBSession.query(func.avg(SquatWorkout.repetitions))
                       .outerjoin(SquatChallenge, SquatChallenge.id==SquatWorkout.challenge_id)
                       .filter(SquatChallenge.percentage==percentage)
                       .filter(SquatWorkout.user_id==self.id)
                       .scalar())
        return repetitions

    def group_average_speed(self, distance):
        '''
        Calculate the average speed by day for a given distance.
        '''
        return (DBSession.query(func.avg(SpeedWorkout.speed), SpeedWorkout.created_at)
                .outerjoin(SpeedChallenge, SpeedChallenge.id==SpeedWorkout.challenge_id)
                .filter(SpeedChallenge.distance==distance)
                .filter(SpeedWorkout.user_id==self.id)
                .group_by(func.day(SpeedWorkout.created_at))
                .all())

    def group_average_heart_rate(self, duration):
        '''
        Calculate the average heart rate by day for a given duration.
        '''
        return (DBSession.query(func.avg(EnduranceWorkout.heart_rate), EnduranceWorkout.created_at)
                .outerjoin(EnduranceChallenge, EnduranceChallenge.id==EnduranceWorkout.challenge_id)
                .filter(EnduranceChallenge.duration==duration)
                .filter(EnduranceWorkout.user_id==self.id)
                .group_by(func.day(EnduranceWorkout.created_at))
                .all())

    def group_average_calories_burned(self, duration):
        '''
        Calculate the average calories burned by day for a given duration.
        '''
        return (DBSession.query(func.avg(EnduranceWorkout.calories_burned), EnduranceWorkout.created_at)
                .outerjoin(EnduranceChallenge, EnduranceChallenge.id==EnduranceWorkout.challenge_id)
                .filter(EnduranceChallenge.duration==duration)
                .filter(EnduranceWorkout.user_id==self.id)
                .group_by(func.day(EnduranceWorkout.created_at))
                .all())

    def group_average_bench_press_repetitions(self, percentage):
        '''
        Calculate the average bench press by day for a given percentage.
        '''
        return (DBSession.query(func.avg(BenchPressWorkout.repetitions), BenchPressWorkout.created_at)
                .outerjoin(BenchPressChallenge, BenchPressChallenge.id==BenchPressWorkout.challenge_id)
                .filter(BenchPressChallenge.percentage==percentage)
                .filter(BenchPressWorkout.user_id==self.id)
                .group_by(func.day(BenchPressWorkout.created_at))
                .all())

    def group_average_squat_repetitions(self, percentage):
        '''
        Calculate the average squat repetitions by day for a given percentage.
        '''
        return (DBSession.query(func.avg(SquatWorkout.repetitions), SquatWorkout.created_at)
                .outerjoin(SquatChallenge, SquatChallenge.id==SquatWorkout.challenge_id)
                .filter(SquatChallenge.percentage==percentage)
                .filter(SquatWorkout.user_id==self.id)
                .group_by(func.day(BenchPressWorkout.created_at))
                .all())

    def get_buddies(self, limit=50, page=1):
        '''
        Return all of this users workout buddies.
        '''
        pager = Pager(page, limit)
        return (self._get_buddies_query()
                .order_by(User.username.asc())
                .limit(pager.limit)
                .offset(pager.offset)
                .all())

    def count_buddies(self):
        '''
        Count how many workout buddies this user has.
        '''
        return self._get_buddies_query().count()

    def is_buddy(self, user):
        '''
        Check whether the given user is a workout buddy.
        '''
        return bool(self._get_buddy(user))

    def add_buddy(self, user):
        '''
        Add the user to the list of workout buddies.
        '''
        buddy = self._get_buddy(user)
        if not buddy:
            Buddy.create(user_id=self.id, buddy_id=user.id)
            notification = NewBuddyNotification.create(user=self)
            notification.add_recipients([user])

    def remove_buddy(self, user):
        '''
        Remove the user from the list of workout buddies.
        '''
        buddy = self._get_buddy(user)
        if buddy:
            buddy.delete()

    def get_challenges(self, limit=50, page=1):
        '''
        Return all challenges this user is apart of (paginated).
        '''
        pager = Pager(page, limit)
        return (self.challenges
                .order_by(Challenge.created_at.desc())
                .limit(pager.limit)
                .offset(pager.offset)
                .all())

    def get_workout_for_challenge(self, challenge):
        '''
        Return this users workout for the given challenge.
        '''
        return (Workout.query
                .filter(Workout.user_id==self.id, Workout.challenge_id==challenge.id)
                .first())

    def count_challenges(self):
        '''
        Count all challenges this user is a competitor in.
        '''
        return self.challenges.count()

    def create_speed_challenge(self, competitor, distance):
        challenge = SpeedChallenge.create(self, distance)
        return self._create_challenge(challenge, competitor)

    def create_endurance_challenge(self, competitor, duration):
        challenge = EnduranceChallenge.create(self, duration)
        return self._create_challenge(challenge, competitor)

    def create_bench_press_challenge(self, competitor, percentage):
        challenge = BenchPressChallenge.create(self, percentage)
        return self._create_challenge(challenge, competitor)

    def create_squat_challenge(self, competitor, percentage):
        challenge = SquatChallenge.create(self, percentage)
        return self._create_challenge(challenge, competitor)

    def create_speed_workout(self, challenge, samples):
        workout = SpeedWorkout.create(self, challenge, samples)
        return self._create_workout(workout)

    def create_endurance_workout(self, challenge, samples):
        workout = EnduranceWorkout.create(self, challenge, samples)
        return self._create_workout(workout)

    def create_bench_press_workout(self, challenge, repetitions):
        workout = BenchPressWorkout.create(self, challenge, repetitions)
        return self._create_workout(workout)

    def create_squat_workout(self, challenge, repetitions):
        workout = SquatWorkout.create(self, challenge, repetitions)
        return self._create_workout(workout)

    def in_challenge(self, challenge):
        '''
        Check whether this user is a competitor in the given challenge.
        '''
        return challenge in self.challenges

    def owns_challenge(self, challenge):
        '''
        Check whether this user is the creator of the given challenge.
        '''
        return self is challenge.creator

    def accepted_challenge(self, challenge):
        '''
        Check whether this user has accepted the given challenge.
        '''
        pivot = self._get_challenge_link(challenge)
        return pivot.is_accepted is True

    def denied_challenge(self, challenge):
        '''
        Check whether this user has denied the given challenge.
        '''
        pivot = self._get_challenge_link(challenge)
        return pivot.is_accepted is False

    def accept_challenge(self, challenge):
        '''
        Change the status between this user and the given challenge to accepted,
        and send all other competitors a notification.
        '''
        pivot = self._get_challenge_link(challenge)
        pivot.accept()
        notification = AcceptedChallengeNotification.create(user=self, challenge=challenge)
        notification.add_recipients(set(challenge.competitors) - set([self]))

    def deny_challenge(self, challenge):
        '''
        Change the status between this user and the given challenge to denied,
        and send all other competitors a notification.
        '''
        pivot = self._get_challenge_link(challenge)
        pivot.deny()
        notification = DeniedChallengeNotification.create(user=self, challenge=challenge)
        notification.add_recipients(set(challenge.competitors) - set([self]))

    def get_all_notifications(self, limit=50, page=1):
        '''
        Return all notifications, regardless of status (paginated).
        '''
        pager = Pager(page, limit)
        return (self._get_notifications_query(unconfirmed_only=False)
                .limit(pager.limit)
                .offset(pager.offset)
                .all())

    def count_all_notifications(self):
        '''
        Count all notifications, regardless of status.
        '''
        return self._get_notifications_query(unconfirmed_only=False).count()

    def get_unconfirmed_notifications(self, limit=50, page=1):
        '''
        Return all notifications which have not been confirmed.
        '''
        pager = Pager(page, limit)
        return (self._get_notifications_query(unconfirmed_only=True)
                .limit(pager.limit)
                .offset(pager.offset)
                .all())

    def count_unconfirmed_notifications(self):
        '''
        Count all notifications which have not been confirmed.
        '''
        return self._get_notifications_query(unconfirmed_only=True).count()

    def confirm_all_notifications(self):
        '''
        Mark all notifications as confirmed (read).
        '''
        unconfirmed_notifications = (
            UserNotification.query.filter(UserNotification.user_id==self.id))
        for notification in unconfirmed_notifications:
            notification.confirm()

    def has_unconfirmed_notifications(self):
        '''
        Check whether this user has any unconfirmed (unread) notifications.
        '''
        return bool(self.count_unconfirmed_notifications())

    @classmethod
    def _get_search_query(cls, terms):
        return cls._get_fulltext_query(terms)

    def _create_challenge(self, challenge, competitor):
        '''
        Add the competitor to the challenge and send them a notification.
        '''
        challenge.add_competitor(competitor)
        notification = RequestedChallengeNotification.create(user=self, challenge=challenge)
        notification.add_recipients([competitor])
        return challenge

    def _create_workout(self, workout):
        '''
        Send the other competitor(s) a notification.
        '''
        notification = UploadedWorkoutNotification.create(user=self, challenge=workout.challenge)
        notification.add_recipients(set(workout.challenge.competitors) - set([self]))
        return workout

    def _get_buddies_query(self):
        '''
        Query for all of this users buddies.
        '''
        users = (User.query
                 .outerjoin(Buddy, Buddy.user_id==User.id)
                 .filter(Buddy.buddy_id==self.id))
        buddies = (User.query
                   .outerjoin(Buddy, Buddy.buddy_id==User.id)
                   .filter(Buddy.user_id==self.id))
        return users.union(buddies)

    def _get_buddy(self, user):
        '''
        Return the buddy link between this user and the given user.
        '''
        return (Buddy.query
                .filter(or_(
                    and_(Buddy.user_id==self.id,
                         Buddy.buddy_id==user.id),
                    and_(Buddy.buddy_id==self.id,
                         Buddy.user_id==user.id)))
                .first())

    def _get_challenge_link(self, challenge):
        '''
        Return the link between this user and the given challenge.
        '''
        return (UserChallenge.query
                .filter(UserChallenge.user_id==self.id, UserChallenge.challenge_id==challenge.id)
                .first())

    def _get_notifications_query(self, unconfirmed_only=True):
        '''
        @param unconfirmed_only Whether to only query for unconfirmed notifications
        '''
        notifications = (Notification.query
                         .outerjoin(UserNotification,
                                    UserNotification.notification_id==Notification.id)
                         .filter(UserNotification.user_id==self.id)
                         .order_by(Notification.created_at.desc()))
        if unconfirmed_only:
            notifications = notifications.filter(UserNotification.is_confirmed==False)
        return notifications


# Avoid circular imports
from wowf.models.challenge import (
    BenchPressChallenge, Challenge, EnduranceChallenge,
    SpeedChallenge, SquatChallenge)
from wowf.models.notification import (
    AcceptedChallengeNotification, DeniedChallengeNotification,
    NewBuddyNotification, Notification, RequestedChallengeNotification,
    UploadedWorkoutNotification)
from wowf.models.pivot_tables import Buddy, UserChallenge, UserNotification
from wowf.models.workout import (
    BenchPressWorkout, EnduranceWorkout, SpeedWorkout,
    SquatWorkout, Workout)