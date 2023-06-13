'''
Auth related helpers used to login, logout, hash passwords, etc.
'''

from __future__ import unicode_literals
import bcrypt
import datetime
import random
import string
from pyramid.response import Response
from pyramid.security import authenticated_userid, forget, remember
from pyramid.threadlocal import get_current_request
from wowf.lib.mailer import send_mail
from wowf.lib.utils import current_timestamp, parse_timedelta
from wowf.models import Group, InviteToken, LoginToken, PasswordToken, User


LOGIN_GROUP = 'login'
DEFAULT_GROUPS = [LOGIN_GROUP]

LOGIN_TOKEN_KEY = 'auth_token'

LOGIN_TOKEN_LIFETIME = datetime.timedelta(days=30)
PASSWORD_TOKEN_LIFETIME = datetime.timedelta(hours=24)
INVITE_TOKEN_LIFETIME = datetime.timedelta(days=30)


class Auth(object):

    @staticmethod
    def send_invite(emails, user=None):
        '''
        Send invitations to the given emails on behalf of the user, if given,
        or on behalf of the system.
        '''
        invite_token = InviteToken.create(user, INVITE_TOKEN_LIFETIME)
        if user:
            extra_headers = {'Reply-To': user.email}
        else:
            extra_headers = None
        send_mail(subject="You've Been Invited To Join Workout With Friends", recipients=emails,
                  template='emails/invite.html',
                  variables=dict(user=user, token=invite_token.token,
                                 age=parse_timedelta(INVITE_TOKEN_LIFETIME)),
                  extra_headers=extra_headers)

    @staticmethod
    def check_invite(token):
        '''
        Check if the token is valid, and thus if the user is allowed to register.
        '''
        invite_token = InviteToken.get_by_token(token)
        return invite_token and invite_token.is_valid()

    @staticmethod
    def register(user, login=True):
        '''
        Provide the user with the minimum privileges necessary to access the
        system.

        @param login Whether to return login headers
        '''
        for group in DEFAULT_GROUPS:
            user.groups.append(Group.get_by_name(group))
        send_mail(subject='Welcome to Workout With Friends', recipients=user.email,
                  template='emails/welcome.html', variables=dict(user=user))
        if login:
            return Auth.login(user, remember_me=False)

    @staticmethod
    def check_login(email, password):
        '''
        Check the email/password combo, and whether the user has privileges
        necessary to access the system.
        '''
        user = User.get_by_email(email)
        if user and user.password == Auth.hash_password(password, user.password):
            login_group = Group.get_by_name(LOGIN_GROUP)
            return user and login_group in user.groups
        return False

    @staticmethod
    def login(user, remember_me=False):
        '''
        Start a new session for the user.

        Performs no authentication on the user, so authenticate the user
        proior to logging them in.

        @return Login response headers
        '''
        request = get_current_request()
        response = Response()
        response.headerlist.extend(remember(request, user.id))
        if remember_me:
            login_token = LoginToken.create(user, LOGIN_TOKEN_LIFETIME, request.user_agent)
            response.set_cookie(LOGIN_TOKEN_KEY, login_token.token, max_age=LOGIN_TOKEN_LIFETIME)
        if not user.is_active:
            user.is_active = True
        user.last_active_at = current_timestamp()
        return response.headers

    @staticmethod
    def auto_login():
        '''
        Log the user in based on the presence of a "remember me" token.

        Only works if the user chose to be remembered on last login, and a
        valid token exists.

        @return Response headers or None
        '''
        request = get_current_request()
        token = request.cookies.get(LOGIN_TOKEN_KEY)
        if token:
            login_token = LoginToken.get_by_token(token)
            if login_token and login_token.is_valid(request.user_agent):
                return Auth.login(login_token.user, remember_me=False)

    @staticmethod
    def logout():
        '''
        End the users session. Delete login token if one is found.

        @return Response headers
        '''
        request = get_current_request()
        response = Response()
        response.headerlist.extend(forget(request))
        auth_token = request.cookies.get(LOGIN_TOKEN_KEY)
        if auth_token:
            response.delete_cookie(LOGIN_TOKEN_KEY)
            token = LoginToken.get_by_token(auth_token)
            if token:
                token.delete()
        return response.headers

    @staticmethod
    def request_reset_password(email):
        '''
        Send an email to the user with unstructions on how to reset their
        password.
        '''
        user = User.get_by_email(email)
        password_token = PasswordToken.create(user, PASSWORD_TOKEN_LIFETIME)
        send_mail(subject='Reset Password Request', recipients=user.email,
                  template='emails/request_password.html',
                  variables=dict(user=user, token=password_token.token,
                                 age=parse_timedelta(PASSWORD_TOKEN_LIFETIME)))

    @staticmethod
    def reset_password(token):
        '''
        Check the token, reset the password of the linked user, and email
        them a copy upon success.

        @return True or False
        '''
        is_success = False
        password_token = PasswordToken.get_by_token(token)
        if password_token and password_token.is_valid():
            random_password = Auth.generate_random_password()
            user = password_token.user
            user.password = random_password
            send_mail(subject='Temporary Password', recipients=user.email,
                      template='emails/temporary_password.html',
                      variables=dict(user=user, random_password=random_password))
            password_token.delete()
            is_success = True
        return is_success

    @staticmethod
    def hash_password(password, check_password=None):
        '''
        Hash the password.

        @param check_password Current password hash, used as salt
        '''
        if isinstance(password, unicode):
            password = password.encode('utf-8')
        if check_password is None:
            # Creating a new password
            salt = bcrypt.gensalt(12)
        else:
            # Checking the current password
            salt = check_password
        return bcrypt.hashpw(password, salt)

    @staticmethod
    def generate_random_password(length=8, chars=None):
        '''
        Returns a random password using the given characters.

        @param chars A sequence of acceptable characters
        '''
        chars = chars or string.letters + string.digits + '!@#$*?'
        return ''.join(random.sample(chars, length))

    @staticmethod
    def get_current_user():
        '''
        Get the currently logged in user.

        @return User instance or None
        '''
        request = get_current_request()
        user_id = authenticated_userid(request)
        if user_id:
            return User.get_by_id(user_id)