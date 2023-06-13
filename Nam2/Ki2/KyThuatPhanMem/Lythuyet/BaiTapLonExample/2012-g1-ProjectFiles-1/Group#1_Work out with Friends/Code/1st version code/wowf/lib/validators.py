'''
Custom WTForms validators.
'''

from __future__ import unicode_literals
import os
from cgi import FieldStorage
from wowf.lib.auth import Auth
from wowf.models import DBSession
from wtforms.validators import Required, ValidationError


class Unique(object):
    '''
    Makes sure that a field does not already exist in the database.

    When editing rows, pass the id of the row as a hidden field so that
    validation does not fail if the field does not change.
    '''

    def __init__(self, model, column, message=None):
        '''
        @param model The model to query
        @param column The column that must be unique
        '''
        self.model = model
        self.column = column
        self.message = message

    def __call__(self, form, field):
        id = None
        if 'id' in form.state:
            id = form.state.id
        found = DBSession.query(self.model).filter(self.column==field.data).first()
        if found and found.id != id:
            if self.message is None:
                self.message = 'Field must be unique.'
            raise ValidationError(self.message)


class Exists(Unique):
    '''
    Makes sure that a field exists in the database.
    '''

    def __call__(self, form, field):
        found = DBSession.query(self.model).filter(self.column==field.data).first()
        if not found:
            if self.message is None:
                self.message = 'Field must exist.'
            raise ValidationError(self.message)


class ValidLogin(object):
    '''
    Makes sure that the email and password combo exists in the database, and
    the user has the necessary priveleges to login.
    '''

    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        if not Auth.check_login(form.email.data, form.password.data):
            if self.message is None:
                self.message = 'Invalid login.'
            raise ValidationError(self.message)


class FileRequired(Required):
    '''
    Makes sure a file was selected and uploaded.
    '''

    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        if not isinstance(field.data, FieldStorage):
            if self.message is None:
                self.message = 'A file is required.'
            raise ValidationError(self.message)


class FileType(object):
    '''
    Makes sure a file is of the proper type.
    '''

    def __init__(self, allowed, message=None):
        self.allowed = [x.upper() for x in allowed]
        self.message = message

    def __call__(self, form, field):
        if isinstance(field.data, FieldStorage):
            ext = os.path.splitext(field.data.filename)[1]
            ext = ext.lstrip('.').upper()
            if ext not in self.allowed:
                if self.message is None:
                    self.message = 'File type must be %(allowed)s.'
                if len(self.allowed) <= 2:
                    allowed = ' or '.join(self.allowed)
                else:
                    allowed = ', '.join(self.allowed[:-1] + ['or ' + self.allowed[-1]])
                self.message = self.message % dict(allowed=allowed)
                raise ValidationError(self.message)