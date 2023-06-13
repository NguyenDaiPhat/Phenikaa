from __future__ import unicode_literals
import hashlib
import uuid
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship, synonym
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import CHAR, DateTime, Integer
from wowf.lib.utils import current_timestamp
from wowf.models import Base


class Token(object):

    id = Column(Integer(unsigned=True), primary_key=True)
    token = Column(CHAR(36), nullable=False, unique=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, nullable=False, default=current_timestamp)
    expires_at = Column(DateTime, nullable=False)

    @declared_attr
    def user_id(cls):
        return Column(
            Integer(unsigned=True), ForeignKey('users.id', ondelete='cascade'),
            nullable=False)

    @declared_attr
    def user(cls):
        return relationship('User', lazy='joined')

    def __init__(self, user, lifetime):
        self.user = user
        self.expires_at = current_timestamp() + lifetime

    def __unicode__(self):
        return self.token

    @classmethod
    def create(cls, user, lifetime):
        return super(Token, cls).create(user=user, lifetime=lifetime)

    @classmethod
    def get_by_token(cls, token):
        return cls.query.filter(cls.token==token).first()

    @classmethod
    def delete_expired(cls):
        cls.query.filter(cls.expires_at<current_timestamp()).delete()

    def is_valid(self):
        return self.user and current_timestamp() < self.expires_at


class LoginToken(Token, Base):
    '''
    Remember me login token.
    '''

    __tablename__ = 'login_tokens'
    _user_agent = Column('user_agent', CHAR(32), nullable=False)

    def _get_user_agent(self):
        return self._user_agent

    def _set_user_agent(self, user_agent):
        '''
        Hash the given user agent.
        '''
        self._user_agent = hashlib.md5(user_agent).hexdigest()

    def _check_user_agent(self, user_agent):
        return self.user_agent == hashlib.md5(user_agent).hexdigest()

    user_agent = synonym('_user_agent', descriptor=property(_get_user_agent, _set_user_agent))

    def __init__(self, user, lifetime, user_agent):
        super(LoginToken, self).__init__(user, lifetime)
        self.user_agent = user_agent

    @classmethod
    def create(cls, user, lifetime, user_agent):
        return super(Token, cls).create(user=user, lifetime=lifetime, user_agent=user_agent)

    def is_valid(self, user_agent):
        return Token.is_valid(self) and self._check_user_agent(user_agent)


class PasswordToken(Token, Base):
    '''
    Reset password token.
    '''

    __tablename__ = 'password_tokens'


class InviteToken(Token, Base):
    '''
    Invite new user token.

    Invitations need not necessarily come from any specific user, so the user
    is optional.
    '''

    __tablename__ = 'invite_tokens'
    user_id = Column(
        Integer(unsigned=True), ForeignKey('users.id', ondelete='cascade'),
        nullable=True)

    def is_valid(self):
        return current_timestamp() < self.expires_at