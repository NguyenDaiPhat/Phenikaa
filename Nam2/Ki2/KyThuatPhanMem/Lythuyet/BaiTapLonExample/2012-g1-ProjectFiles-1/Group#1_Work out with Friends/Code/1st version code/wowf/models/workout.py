from __future__ import unicode_literals
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import backref, relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import DateTime, Integer, Numeric, SmallInteger
from wowf.lib.utils import current_timestamp
from wowf.models.lookup_tables import ChallengeType
from wowf.models.meta import Base


class Workout(Base):

    __tablename__ = 'workouts'
    __mapper_args__ = {'polymorphic_on': 'challenge_type_id', 'with_polymorphic': '*'}
    id = Column(Integer(unsigned=True), primary_key=True)
    user_id = Column(Integer(unsigned=True), ForeignKey('users.id'), nullable=False)
    challenge_id = Column(Integer(unsigned=True), ForeignKey('challenges.id'), nullable=False)
    challenge_type_id = Column(
        Integer(unsigned=True), ForeignKey('challenge_types.id', ondelete='cascade'),
        nullable=False)
    points = Column(SmallInteger(unsigned=True), nullable=False)
    created_at = Column(DateTime, nullable=False, default=current_timestamp)

    user = relationship(
        'User', lazy='joined', backref=backref('workouts', lazy='dynamic'))
    challenge = relationship(
        'Challenge', lazy='joined', backref=backref('workouts', lazy='dynamic'))


class _Workout(object):

    @declared_attr
    def id(cls):
        return Column(
            Integer(unsigned=True), ForeignKey('workouts.id', ondelete='cascade'),
            primary_key=True)


class DeviceWorkout(_Workout):
    '''
    Base class for all workouts which require the use of a heart rate device.
    '''

    @classmethod
    def create(cls, user, challenge, samples):
        return super(DeviceWorkout, cls).create(
            user=user, challenge=challenge, samples=samples)


class WeightWorkout(_Workout):
    '''
    Base class for all weight related workouts.
    '''

    repetitions = Column(SmallInteger(unsigned=True), nullable=False)

    @classmethod
    def create(cls, user, challenge, repetitions):
        return super(WeightWorkout, cls).create(
            user=user, challenge=challenge, repetitions=repetitions)


class SpeedWorkout(DeviceWorkout, Workout):

    __tablename__ = 'speed_workouts'
    __mapper_args__ = {'polymorphic_identity': ChallengeType.lookup_data.index('speed') + 1}
    speed = Column(Numeric(4, 2), nullable=False, doc='speed in meters per second')

    def __init__(self, user, challenge, samples):
        self.user = user
        self.challenge = challenge
        total_distance = samples['distance'][-1]
        if not total_distance >= challenge.distance:
            # Did not run the full distance
            self.points = self.speed = 0
            return
        distance_samples = zip(samples['timestamp'], samples['distance'])
        distance = time = 0
        for t, d in distance_samples:
            if d >= challenge.distance:
                time = t
                distance = d
        time = time / 1000.00 # Convert to seconds
        self.speed = float(distance / time)
        self.points = self.speed * 100
        avg_speed = user.get_average_speed(challenge.distance)
        if avg_speed:
            delta = 100 * float(self.speed - avg_speed) / avg_speed
            if delta >= 10:
                # 10% increase
                self.points *= 1.1
            elif delta <= 10:
                # 10% decline
                self.points *= 0.9


class EnduranceWorkout(DeviceWorkout, Workout):

    __tablename__ = 'endurance_workouts'
    __mapper_args__ = {'polymorphic_identity': ChallengeType.lookup_data.index('endurance') + 1}
    heart_rate = Column(SmallInteger(unsigned=True), nullable=False)
    calories_burned = Column(SmallInteger(unsigned=True), nullable=False)

    def __init__(self, user, challenge, samples):
        self.user = user
        self.challenge = challenge
        total_duration = samples['timestamp'][-1] / 1000.0
        total_duration = total_duration / 60.0
        if not total_duration >= challenge.duration:
            # Did not run the full duration
            self.points = self.heart_rate = self.calories_burned = 0
            return
        duration = challenge.duration * 60.0 * 1000.0 # Convert to microseconds
        heart_rate_samples = zip(samples['timestamp'], samples['heart_rate'])
        calories_burned_samples = zip(samples['timestamp'], samples['calories_burned'])
        heart_rate = []
        calories_burned = 0
        for t, h in heart_rate_samples:
            heart_rate.append(h)
            if t >= duration:
                break
        for t, c in calories_burned_samples:
            if t >= duration:
                calories_burned = c
        self.heart_rate = float(sum(heart_rate)) / len(heart_rate)
        self.calories_burned = calories_burned
        self.points = self.heart_rate * 10 + self.calories_burned
        avg_heart_rate = user.get_average_heart_rate(challenge.duration)
        avg_calories_burned = user.get_average_calories_burned(challenge.duration)
        if avg_heart_rate:
            delta = 100 * float(self.heart_rate - avg_heart_rate) / avg_heart_rate
            if delta >= 10:
                # 10% increase
                self.points *= 1.05
            elif delta <= 10:
                # 10% decline
                self.points *= 0.95
        if avg_calories_burned:
            delta = 100 * float(self.calories_burned - avg_calories_burned) / avg_calories_burned
            if delta >= 10:
                # 10% increase
                self.points *= 1.05
            elif delta <= 10:
                # 10% decline
                self.points *= 0.95


class BenchPressWorkout(WeightWorkout, Workout):

    __tablename__ = 'bench_press_workouts'
    __mapper_args__ = {'polymorphic_identity': ChallengeType.lookup_data.index('bench_press') + 1}

    def __init__(self, user, challenge, repetitions):
        self.user = user
        self.challenge = challenge
        self.repetitions = repetitions
        self.points = challenge.calculate_user_weight(user) * repetitions
        avg_repetitions = user.get_average_bench_press_repetitions(challenge.percentage)
        if avg_repetitions:
            delta = 100 * float(self.repetitions - avg_repetitions) / avg_repetitions
            if delta >= 10:
                # 10% increase
                self.points *= 1.1
            elif delta <= 10:
                # 10% decline
                self.points *= 0.9
        # Scale down for bench press
        self.points *= 0.9


class SquatWorkout(WeightWorkout, Workout):

    __tablename__ = 'squat_workouts'
    __mapper_args__ = {'polymorphic_identity': ChallengeType.lookup_data.index('squat') + 1}

    def __init__(self, user, challenge, repetitions):
        self.user = user
        self.challenge = challenge
        self.repetitions = repetitions
        self.points = challenge.calculate_user_weight(user) * repetitions
        avg_repetitions = user.get_average_squat_repetitions(challenge.percentage)
        if avg_repetitions:
            delta = 100 * float(repetitions - avg_repetitions) / avg_repetitions
            if delta >= 10:
                # 10% increase
                self.points *= 1.1
            elif delta <= 10:
                # 10% decline
                self.points *= 0.9
        # Scale down for squat
        self.points *= 0.9