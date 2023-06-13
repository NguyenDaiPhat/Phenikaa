from __future__ import unicode_literals
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config, view_defaults
from wowf.forms import ChangePasswordForm, ResetPasswordForm, State, UpdateProfileForm
from wowf.lib.auth import Auth
from wowf.views import BaseView


@view_defaults(route_name='account.profile', permission='member')
class UpdateProfileView(BaseView):

    @view_config(renderer='account/profile.html')
    def main(self):
        form = UpdateProfileForm(
            self.request.POST, obj=self.request.user, state=State(id=self.request.user.id))
        if 'update_profile' in self.request.POST and form.validate():
            form.update_profile(self.request.user)
            self.request.session.flash('Profile saved successfully.', self.consts.SUCCESS)
            return HTTPFound(location=self.request.path)
        return dict(form=form)


@view_defaults(route_name='account.password', permission='member')
class ChangePasswordView(BaseView):

    @view_config(renderer='account/password.html')
    def main(self):
        form = ChangePasswordForm(
            self.request.POST, state=State(password=self.request.user.password))
        if 'change_password' in self.request.POST and form.validate():
            form.update_password(self.request.user)
            self.request.session.flash('Password saved successfully.', self.consts.SUCCESS)
            return HTTPFound(location=self.request.path)
        return dict(form=form)


@view_defaults(route_name='account.password.request', permission='guest')
class RequestPasswordView(BaseView):

    @view_config(renderer='account/request_password.html')
    def main(self):
        form = ResetPasswordForm(self.request.POST)
        if 'reset_password' in self.request.POST and form.validate():
            form.request_reset_password()
            self.request.session.flash('Check your email for further instructions.', self.consts.NOTICE)
            return HTTPFound(location=self.request.path)
        return dict(form=form)


@view_defaults(route_name='account.password.reset', permission='guest')
class ResetPasswordView(BaseView):

    @view_config()
    def main(self):
        token = self.request.matchdict['token']
        if Auth.reset_password(token):
            self.request.session.flash('Check your email for a temporary password.', self.consts.NOTICE)
            return HTTPFound(location=self.request.route_url(
                'user.login', _query={'return_to': self.request.route_url('account.password')}))
        else:
            self.request.session.flash('The token provided was either invalid or expired. Please try again.', self.consts.ERROR)
            return HTTPFound(location=self.request.route_url('account.password.request'))