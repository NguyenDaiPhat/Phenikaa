from __future__ import unicode_literals
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import backref, relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import DateTime, Integer, Numeric, SmallInteger
from wowf.lib.utils import current_timestamp
from wowf.models.lookup_tables import ChallengeType
from wowf.models.meta import Base
from wowf.models.pivot_tables import UserChallenge


class Challenge(Base):
    '''
    Base class for ALL challenges.
    '''

    __tablename__ = 'challenges'
    __mapper_args__ = {'polymorphic_on': 'challenge_type_id', 'with_polymorphic': '*'}
    id = Column(Integer(unsigned=True), primary_key=True)
    user_id = Column(Integer(unsigned=True), ForeignKey('users.id'), nullable=False)
    challenge_type_id = Column(
        Integer(unsigned=True), ForeignKey('challenge_types.id', ondelete='cascade'),
        nullable=False)
    created_at = Column(DateTime, nullable=False, default=current_timestamp)

    _creator = relationship('User', lazy='joined')
    competitors = relationship(
        'User', backref=backref('challenges', lazy='dynamic'),
        secondary='users_challenges', lazy='dynamic')

    def _get_creator(self):
        return self._creator

    def _set_creator(self, creator):
        '''
        Set the creator, and accept the challenge for him.
        '''
        self._creator = creator
        pivot = UserChallenge.create(creator, self)
        pivot.accept()

    creator = property(_get_creator, _set_creator)

    def add_competitor(self, user):
        '''
        Add the user to the list of competitors.
        '''
        if user not in self.competitors:
            self.competitors.append(user)

    def remove_competitor(self, user):
        '''
        Remove the user from the list of competitors.
        '''
        if user in self.competitors:
            self.competitors.remove(user)

    def is_device_challenge(self):
        '''
        Check if the challenge requires the use of a heart rate device.
        '''
        return isinstance(self, DeviceChallenge)

    def is_weight_challenge(self):
        '''
        Check if the challenge is a weight lifting challenge.
        '''
        return isinstance(self, WeightChallenge)

    def is_speed_challenge(self):
        '''
        Check if the challenge is a speed challenge.
        '''
        return isinstance(self, SpeedChallenge)

    def is_endurance_challenge(self):
        '''
        Check if the challenge is an endurance challenge.
        '''
        return isinstance(self, EnduranceChallenge)

    def is_bench_press_challenge(self):
        '''
        Check if the challenge is a bench press challenge.
        '''
        return isinstance(self, BenchPressChallenge)

    def is_squat_challenge(self):
        '''
        Check if the challenge is a squat challenge.
        '''
        return isinstance(self, SquatChallenge)

    def is_completed(self):
        '''
        Check if both competitors have uploaded a workout.
        '''
        return self.workouts.count() == 2

    def user_is_winner(self, user):
        '''
        Check if given user is the winner of the challenge.
        '''
        if self.is_completed():
            winning_workout = self.workouts.order_by(Workout.points.desc()).first()
            return user is winning_workout.user

class _Challenge(object):
    '''
    Used for SQLAlchemys joined table inheritance (polymorphism).
    '''

    @declared_attr
    def id(cls):
        return Column(
            Integer(unsigned=True), ForeignKey('challenges.id', ondelete='cascade'),
            primary_key=True)


class DeviceChallenge(_Challenge):
    '''
    Base class for all challenges which require the use of a heart rate device.
    '''
    pass


class WeightChallenge(_Challenge):
    '''
    Base class for all weight related challenges.
    '''

    percentage = Column(Numeric(3, 2), nullable=False, doc='percentage of body weight')

    @classmethod
    def create(cls, creator, percentage):
        return super(WeightChallenge, cls).create(creator=creator, percentage=percentage)

    def calculate_user_weight(self, user):
        '''
        How much weight this user needs to lift for this competition.
        '''
        return round(self.percentage * user.weight, 2)


class SpeedChallenge(DeviceChallenge, Challenge):

    __tablename__ = 'speed_challenges'
    __mapper_args__ = {'polymorphic_identity': ChallengeType.lookup_data.index('speed') + 1}
    distance = Column(SmallInteger(unsigned=True), nullable=False, doc='distance in meters')

    @property
    def description(self):
        return 'Sprint %d meters as fast as you can. The person with the fastest time wins.' % (
            self.distance)

    def __unicode__(self):
        return '%d meter speed challenge' % self.distance

    @classmethod
    def create(cls, creator, distance):
        return super(SpeedChallenge, cls).create(creator=creator, distance=distance)


class EnduranceChallenge(DeviceChallenge, Challenge):

    __tablename__ = 'endurance_challenges'
    __mapper_args__ = {'polymorphic_identity': ChallengeType.lookup_data.index('endurance') + 1}
    duration = Column(SmallInteger(unsigned=True), nullable=False, doc='duration in minutes')

    @property
    def description(self):
        return 'Run as hard as you can for %d minutes. The person with the highest vitals wins.' % (
            self.duration)

    def __unicode__(self):
        return '%d minute endurance challenge' % self.duration

    @classmethod
    def create(cls, creator, duration):
        return super(EnduranceChallenge, cls).create(creator=creator, duration=duration)


class BenchPressChallenge(WeightChallenge, Challenge):

    __tablename__ = 'bench_press_challenges'
    __mapper_args__ = {'polymorphic_identity': ChallengeType.lookup_data.index('bench_press') + 1}

    @property
    def description(self):
        return 'Bench press %d%% of your body weight for as many repetitions as you can. The person with the most repetitions wins.' % (
            self.percentage * 100)

    def __unicode__(self):
        return '%d%% bench press challenge' % (self.percentage * 100)


class SquatChallenge(WeightChallenge, Challenge):

    __tablename__ = 'squat_challenges'
    __mapper_args__ = {'polymorphic_identity': ChallengeType.lookup_data.index('squat') + 1}

    @property
    def description(self):
        return 'Squat %d%% of your body weight for as many repetitions as you can. The person with the most repetitions wins.' % (
            self.percentage * 100)

    def __unicode__(self):
        return '%d%% squat challenge' % (self.percentage * 100)


from wowf.models.workout import Workout