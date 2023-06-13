from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.view import view_config, view_defaults
from wowf.forms import (
    AddBuddyForm, ConfirmNotificationsForm, LoginForm, RegistrationForm,
    RemoveBuddyForm, SendInviteForm, AddRemoveBuddyForm)
from wowf.lib.auth import Auth
from wowf.models import User
from wowf.views import (
    BaseView, get_all_notification_stream, get_buddies_stream,
    get_challenge_stream, get_unconfirmed_notification_stream)


notification_view_streams = {'user.notifications.unconfirmed': get_unconfirmed_notification_stream,
                             'user.notifications.all': get_all_notification_stream}

profile_view_streams = {'user.view.challenges': get_challenge_stream,
                        'user.view.buddies': get_buddies_stream}


@view_defaults(permission='member')
class NotificationView(BaseView):

    @view_config(route_name='user.notifications.unconfirmed', renderer='user/notifications/unconfirmed.html')
    @view_config(route_name='user.notifications.all', renderer='user/notifications/all.html')
    def main(self):
        form = ConfirmNotificationsForm(self.request.POST)
        if 'confirm_notifications' in self.request.POST and form.validate():
            form.confirm_notifications(self.request.user)
            return HTTPFound(location=self.request.route_url('user.notifications.unconfirmed'))
        stream = notification_view_streams[self.request.matched_route.name](self.request.user)
        return dict(form=form,
                    stream=stream)


@view_defaults(permission='member')
class ProfileView(BaseView):

    @view_config(route_name='user.view.challenges', renderer='user/view/challenges.html')
    @view_config(route_name='user.view.buddies', renderer='user/view/buddies.html')
    def main(self):
        user = User.get_by_id(self.request.matchdict['id'])
        if not user:
            raise HTTPNotFound()
        add_remove_buddy_form = None
        if not self.request.user.is_user(user):
            add_remove_buddy_form = AddRemoveBuddyForm(self.request.POST)
            if 'add' in self.request.POST:
                add_remove_buddy_form.add_buddy(self.request.user, user)
                return HTTPFound(location=self.request.path)
            elif 'remove' in self.request.POST:
                add_remove_buddy_form.remove_buddy(self.request.user, user)
                return HTTPFound(location=self.request.path)
        stream = profile_view_streams[self.request.matched_route.name](user)
        return dict(user=user,
                    add_remove_buddy_form=add_remove_buddy_form,
                    stream=stream)


@view_defaults(route_name='user.logout')
class LogoutView(BaseView):

    @view_config()
    def main(self):
        headers = Auth.logout()
        return HTTPFound(location=self.request.route_url('user.login'), headers=headers)


@view_defaults(route_name='user.login', permission='guest')
class LoginView(BaseView):

    @view_config(renderer='user/login.html')
    def main(self):
        form = LoginForm(self.request.POST)
        if 'login' in self.request.POST and form.validate():
            headers = form.login_user()
            location = self.request.GET.get(
                'return_to', self.request.route_url('home'))
            return HTTPFound(location=location, headers=headers)
        return dict(form=form)


@view_defaults(route_name='user.register', permission='guest')
class RegisterView(BaseView):

    @view_config(renderer='user/register.html')
    def main(self):
        form = RegistrationForm(self.request.POST)
        if 'registration' in self.request.POST and form.validate():
            headers = form.register_user()
            self.request.session.flash("Welcome to Workout With Friends!", self.consts.SUCCESS)
            return HTTPFound(location=self.request.route_url('home'), headers=headers)
        return dict(form=form)


@view_defaults(route_name='user.invite', permission='member')
class SendInviteView(BaseView):

    @view_config(renderer='user/invite.html')
    def main(self):
        form = SendInviteForm(self.request.POST)
        if 'send_invite' in self.request.POST and form.validate():
            form.send_invite_email(self.request.user)
            self.request.session.flash('An invitation has been sent out on your behalf.', self.consts.SUCCESS)
            return HTTPFound(location=self.request.path)
        return dict(form=form)