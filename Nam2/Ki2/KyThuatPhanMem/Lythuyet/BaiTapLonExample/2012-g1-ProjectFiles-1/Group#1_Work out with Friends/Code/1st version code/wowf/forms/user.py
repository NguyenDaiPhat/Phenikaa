from __future__ import unicode_literals
from cgi import FieldStorage
from timezones import zones
from wowf.forms import Form
from wowf.lib.auth import Auth
from wowf.lib.fields import EmailField
from wowf.lib.utils import years_ago
from wowf.lib.validators import FileType, Unique, ValidLogin
from wowf.models import User
from wtforms import validators
from wtforms.fields import (
    BooleanField, DateField, DecimalField, FieldList, FileField,
    PasswordField, SelectField, SubmitField, TextField)


MIN_AGE = 13


def get_genders():
    return [('', 'Select Gender'), ('F', 'Female'), ('M', 'Male')]


def get_timezones():
    timezones = [('', 'Select Timezone')]
    for _, name, formatted_name in zones.get_timezones(only_us=True):
        timezones.append([name, formatted_name])
    return timezones


class UserForm(Form):

    username = TextField('Username', [
        validators.Required(message='Username cannot be blank'),
        validators.Length(min=5, max=10, message='Limit username to between %(min)d and %(max)d characters'),
        Unique(User, User.username, message='Username is already in use')])
    email = EmailField('Email', [
        validators.Required(message='Email cannot be blank'),
        validators.Email(message='Valid email address is required'),
        Unique(User, User.email, message='Email is already in use')])
    gender = SelectField('Gender', [
        validators.Required(message='Must select a gender')],
        choices=get_genders())
    dob = DateField('Date of Birth', [
        validators.Required('Date of Birth cannot be blank')],
        format='%m/%d/%y', description='mm/dd/yy')
    weight = DecimalField('Weight (kg)', [
        validators.Required(message='Weight must be a positive number'),
        validators.NumberRange(min=0, message='Weight must be at least %(min)d kilograms')])
    height = DecimalField('Height (m)', [
        validators.Required(message='Height must be a positive number'),
        validators.NumberRange(min=0, message='Height must be at least %(min)d meters')])

    def validate_dob(self, field):
        if years_ago(field.data) < MIN_AGE:
            raise validators.ValidationError('You must be %d or older to join' % MIN_AGE)


class RegistrationForm(UserForm):

    password = PasswordField('Password', [
        validators.Required('Password cannot be blank'),
        validators.Length(min=6, max=15, message='Password must be between %(min)d and %(max)d characters')])

    def register_user(self):
        '''
        @return Login response headers
        '''
        user = User.create(
            self.username.data, self.email.data, self.password.data, self.gender.data,
            self.dob.data, self.weight.data, self.height.data)
        return Auth.register(user, login=True)


class UpdateProfileForm(UserForm):

    timezone = SelectField('Timezone', choices=get_timezones())
    avatar = FileField('Profile image', [
        FileType(['gif', 'jpg', 'jpeg', 'png'], message='Profile image must be a %(allowed)s')])

    def update_profile(self, user):
        user.update_profile(
            self.username.data, self.email.data, self.gender.data, self.dob.data,
            self.weight.data, self.height.data, self.timezone.data)
        if isinstance(self.avatar.data, FieldStorage):
            user.update_avatar(self.avatar.data)


class LoginForm(Form):

    email = EmailField('Email', [
        validators.Required('Email cannot be blank'),
        ValidLogin(message='Invalid email/password combo')])
    password = PasswordField('Password', [
        validators.Required('Password cannot be blank')])
    remember_me = BooleanField('Remember me', default=True)

    def login_user(self):
        '''
        @return Login response headers
        '''
        user = User.get_by_email(self.email.data)
        return Auth.login(user, self.remember_me.data)


class ChangePasswordForm(Form):

    current_password = PasswordField('Current password', [
        validators.Required(message='Current password cannot be blank')])
    new_password = PasswordField('New password', [
        validators.Required(message='New password cannot be blank'),
        validators.Length(min=6, max=15, message='New password must be between %(min)d and %(max)d characters')])
    confirm_new_password = PasswordField('Verify password', [
        validators.EqualTo('new_password', message='Passwords must match')])

    def validate_current_password(self, field):
        '''
        User must know current password.
        '''
        if self.state.password != Auth.hash_password(field.data, self.state.password):
            raise validators.ValidationError('Invalid current password')

    def validate_new_password(self, field):
        '''
        New password must be different from current password.
        '''
        if field.data == self.current_password.data:
            raise validators.ValidationError('New password must be different from current password')

    def update_password(self, user):
        user.update_password(self.new_password.data)


class AddBuddyForm(Form):

    change_status = SubmitField('Add Buddy')

    def add_buddy(self, user, other_user):
        user.add_buddy(other_user)


class RemoveBuddyForm(Form):

    change_status = SubmitField('Remove Buddy')

    def remove_buddy(self, user, other_user):
        user.remove_buddy(other_user)


class AddRemoveBuddyForm(Form):

    add = SubmitField('Add Buddy')
    remove = SubmitField('Remove Buddy')

    def add_buddy(self, user, other_user):
        user.add_buddy(other_user)

    def remove_buddy(self, user, other_user):
        user.remove_buddy(other_user)


class ResetPasswordForm(Form):

    email = EmailField('Account email', [
        validators.Required(message='Email cannot be blank')])

    def validate_email(self, field):
        '''
        Email must exist.
        '''
        if not User.get_by_email(field.data):
            raise validators.ValidationError('Email could not be found')

    def request_reset_password(self):
        '''
        Send instructions to email on how to reset password.
        '''
        Auth.request_reset_password(self.email.data)


class ConfirmNotificationsForm(Form):

    def confirm_notifications(self, user):
        user.confirm_all_notifications()


class SendInviteForm(Form):

    emails = FieldList(
        EmailField('Email', [
            validators.Email(message='Valid email address is required')]),
        min_entries=1, max_entries=10)

    def send_invite_email(self, user):
        '''
        Send the invite emails, from the user.
        '''
        Auth.send_invite(self.emails.data, user)