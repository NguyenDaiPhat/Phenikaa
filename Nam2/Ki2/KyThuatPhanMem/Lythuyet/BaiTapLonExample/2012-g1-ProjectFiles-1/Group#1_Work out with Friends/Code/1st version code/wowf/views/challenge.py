from __future__ import unicode_literals
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.view import view_config, view_defaults
from wowf.forms import (
    AcceptDenyChallengeForm, CreateBenchPressChallengeForm, CreateEnduranceChallengeForm,
    CreateSpeedChallengeForm, CreateSquatChallengeForm, UploadBenchPressWorkoutForm,
    UploadEnduranceWorkoutForm, UploadSpeedWorkoutForm, UploadSquatWorkoutForm)
from wowf.models import Challenge
from wowf.views import BaseView


create_challenge_forms = {'challenge.create.speed': CreateSpeedChallengeForm,
                          'challenge.create.endurance': CreateEnduranceChallengeForm,
                          'challenge.create.bench': CreateBenchPressChallengeForm,
                          'challenge.create.squat': CreateSquatChallengeForm}


@view_defaults(route_name='challenge.view', permission='member')
class ChallengeView(BaseView):

    @view_config(renderer='challenge/view.html')
    def main(self):
        challenge = Challenge.get_by_id(self.request.matchdict['id'])
        if not challenge:
            raise HTTPNotFound()
        accept_deny_challenge_form = None
        upload_workout_form = None
        if self.request.user.in_challenge(challenge):
            if not (self.request.user.accepted_challenge(challenge) or self.request.user.denied_challenge(challenge)):
                accept_deny_challenge_form = AcceptDenyChallengeForm(self.request.POST)
                if 'accept' in self.request.POST:
                    accept_deny_challenge_form.accept_challenge(self.request.user, challenge)
                    return HTTPFound(location=self.request.path)
                elif 'deny' in self.request.POST:
                    accept_deny_challenge_form.deny_challenge(self.request.user, challenge)
                    return HTTPFound(location=self.request.path)
            elif self.request.user.accepted_challenge(challenge):
                if challenge.is_speed_challenge():
                    upload_workout_form = UploadSpeedWorkoutForm(self.request.POST)
                elif challenge.is_endurance_challenge():
                    upload_workout_form = UploadEnduranceWorkoutForm(self.request.POST)
                elif challenge.is_bench_press_challenge():
                    upload_workout_form = UploadBenchPressWorkoutForm(self.request.POST)
                elif challenge.is_squat_challenge():
                    upload_workout_form = UploadSquatWorkoutForm(self.request.POST)
                if upload_workout_form and 'upload_workout' in self.request.POST and upload_workout_form.validate():
                    upload_workout_form.upload_workout(self.request.user, challenge)
                    return HTTPFound(location=self.request.path)
        return dict(challenge=challenge,
                    accept_deny_challenge_form=accept_deny_challenge_form,
                    upload_workout_form=upload_workout_form)


@view_defaults(permission='member')
class CreateChallengeView(BaseView):

    @view_config(route_name='challenge.create.speed', renderer='challenge/create/speed.html')
    @view_config(route_name='challenge.create.endurance', renderer='challenge/create/endurance.html')
    @view_config(route_name='challenge.create.bench', renderer='challenge/create/bench.html')
    @view_config(route_name='challenge.create.squat', renderer='challenge/create/squat.html')
    def main(self):
        form = create_challenge_forms[self.request.matched_route.name](self.request.POST)
        if 'create_challenge' in self.request.POST and form.validate():
            challenge = form.create_challenge(self.request.user)
            self.request.session.flash('%s has been notified of this challenge.' % form.competitor.data, self.consts.SUCCESS)
            return HTTPFound(location=self.request.route_url('challenge.view', id=challenge.id))
        return dict(form=form)