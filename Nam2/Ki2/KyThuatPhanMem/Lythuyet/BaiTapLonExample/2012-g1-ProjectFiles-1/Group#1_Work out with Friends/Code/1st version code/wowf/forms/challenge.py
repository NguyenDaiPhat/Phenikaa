from __future__ import unicode_literals
from wowf.forms import Form
from wowf.lib.validators import Exists
from wowf.models import User
from wtforms import validators
from wtforms.fields import SelectField, SubmitField, TextField


def get_distances(start=100, max=3200):
    distances = []
    x = start
    while x <= max:
        distances.append((x, '%s meters' % x))
        x *= 2
    return distances


def get_durations(increments=15, max=180):
    return [(x, '%s minutes' % x) for x in range(increments, max + 1, increments)]


def get_percentages(increments=10, max=300):
    return [(x / 100.0, '%s%% of body weight' % x) for x in range(increments, max + 1, increments)]


class CreateChallengeForm(Form):

    competitor = TextField('Competitor', [
        validators.Required('Competitor cannot be blank'),
        Exists(User, User.username, message='Competitor does not exist')],
        description='type in users username')


class CreateDeviceChallengeForm(CreateChallengeForm):
    pass


class CreateWeightChallengeForm(CreateChallengeForm):

    percentage = SelectField('Percentage', [
        validators.Required(message='Must select a percentage')],
        choices=get_percentages(), coerce=float)


class CreateSpeedChallengeForm(CreateDeviceChallengeForm):

    distance = SelectField('Distance', [
        validators.Required(message='Must select a distance')],
        choices=get_distances(), coerce=int)

    def create_challenge(self, user):
        competitor = User.get_by_username(self.competitor.data)
        challenge = user.create_speed_challenge(competitor, self.distance.data)
        return challenge


class CreateEnduranceChallengeForm(CreateDeviceChallengeForm):

    duration = SelectField('Duration', [
        validators.Required(message='Must select a duration')],
        choices=get_durations(), coerce=int)

    def create_challenge(self, user):
        competitor = User.get_by_username(self.competitor.data)
        challenge = user.create_endurance_challenge(competitor, self.duration.data)
        return challenge


class CreateBenchPressChallengeForm(CreateWeightChallengeForm):

    def create_challenge(self, user):
        competitor = User.get_by_username(self.competitor.data)
        challenge = user.create_bench_press_challenge(competitor, self.percentage.data)
        return challenge


class CreateSquatChallengeForm(CreateWeightChallengeForm):

    def create_challenge(self, user):
        competitor = User.get_by_username(self.competitor.data)
        challenge = user.create_squat_challenge(competitor, self.percentage.data)
        return challenge


class AcceptDenyChallengeForm(Form):

    accept = SubmitField('Accept Challenge')
    deny = SubmitField('Deny Challenge')

    def accept_challenge(self, user, challenge):
        user.accept_challenge(challenge)

    def deny_challenge(self, user, challenge):
        user.deny_challenge(challenge)