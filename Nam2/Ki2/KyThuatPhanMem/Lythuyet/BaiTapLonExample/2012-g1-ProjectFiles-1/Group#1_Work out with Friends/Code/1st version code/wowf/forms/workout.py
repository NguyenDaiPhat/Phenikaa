from __future__ import unicode_literals
from cgi import FieldStorage
from wowf.forms import Form
from wowf.lib.utils import parse_workout_report
from wowf.lib.validators import FileType
from wtforms import validators
from wtforms.fields import FileField, IntegerField


class UploadWorkoutForm(Form):
    pass


class UploadDeviceWorkoutForm(UploadWorkoutForm):

    _samples = {}
    workout_report = FileField('Workout report', [
        FileType(['csv'], message='Workout report must be a %(allowed)s')])

    def validate_workout_report(self, field):
        if not isinstance(field.data, FieldStorage):
            raise validators.ValidationError('Must upload workout report')
        self._samples = parse_workout_report(field.data.file)
        if not (self._samples and self._samples['timestamp']):
            raise validators.ValidationError('Workout report is invalid format')


class UploadWeightWorkoutForm(UploadWorkoutForm):

    repetitions = IntegerField('Repetitions', [
        validators.Required(message='Must enter your repetitions'),
        validators.NumberRange(min=0, message='Repetitions must be at least %(min)d')])


class UploadSpeedWorkoutForm(UploadDeviceWorkoutForm):

    def upload_workout(self, user, challenge):
        workout = user.create_speed_workout(challenge, self._samples)
        return workout


class UploadEnduranceWorkoutForm(UploadDeviceWorkoutForm):

    def upload_workout(self, user, challenge):
        workout = user.create_endurance_workout(challenge, self._samples)
        return workout


class UploadBenchPressWorkoutForm(UploadWeightWorkoutForm):

    def upload_workout(self, user, challenge):
        workout = user.create_bench_press_workout(challenge, self.repetitions.data)
        return workout


class UploadSquatWorkoutForm(UploadWeightWorkoutForm):

    def upload_workout(self, user, challenge):
        workout = user.create_squat_workout(challenge, self.repetitions.data)
        return workout