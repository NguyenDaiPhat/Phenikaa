from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer
from wowf.models.meta import Base


class Buddy(Base):
    '''
    Pivot table between users and the users they follow.
    '''

    __tablename__ = 'buddies'
    user_id = Column(
        Integer(unsigned=True), ForeignKey('users.id', ondelete='cascade'),
        primary_key=True, autoincrement=False)
    buddy_id = Column(
        Integer(unsigned=True), ForeignKey('users.id', ondelete='cascade'),
        primary_key=True, autoincrement=False)


class UserChallenge(Base):
    '''
    Pivot table between users and the challenges they are in.
    '''

    __tablename__ = 'users_challenges'
    user_id = Column(
        Integer(unsigned=True), ForeignKey('users.id', ondelete='cascade'),
        primary_key=True, autoincrement=False)
    challenge_id = Column(
        Integer(unsigned=True), ForeignKey('challenges.id', ondelete='cascade'),
        primary_key=True, autoincrement=False)
    is_accepted = Column(Boolean, default=None)

    user = relationship('User', lazy='joined')
    challenge = relationship('Challenge', lazy='joined')

    def __init__(self, user, challenge):
        self.user = user
        self.challenge = challenge

    @classmethod
    def create(cls, user, challenge):
        return super(UserChallenge, cls).create(user=user, challenge=challenge)

    def accept(self):
        self.is_accepted = True

    def deny(self):
        self.is_accepted = False


class UserNotification(Base):
    '''
    Pivot table between users and the notifications they should receive.
    '''

    __tablename__ = 'users_notifications'
    notification_id = Column(
        Integer(unsigned=True),
        ForeignKey('notifications.id', ondelete='cascade'),
        primary_key=True, autoincrement=False)
    user_id = Column(
        Integer(unsigned=True), ForeignKey('users.id', ondelete='cascade'),
        primary_key=True, autoincrement=False)
    is_confirmed = Column(Boolean, nullable=False, default=False)

    def confirm(self):
        self.is_confirmed = True


class UserGroup(Base):
    '''
    Pivot table between users and the groups they belong to.
    '''

    __tablename__ = 'users_groups'
    user_id = Column(
        Integer(unsigned=True), ForeignKey('users.id', ondelete='cascade'),
        primary_key=True, autoincrement=False)
    group_id = Column(
        Integer(unsigned=True), ForeignKey('groups.id', ondelete='cascade'),
        primary_key=True, autoincrement=False)