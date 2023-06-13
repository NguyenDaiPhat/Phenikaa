from __future__ import unicode_literals
from pyramid.threadlocal import get_current_request
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import backref, relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import DateTime, Integer
from webhelpers.html.tags import link_to
from wowf.lib.utils import current_timestamp
from wowf.models.lookup_tables import NotificationType
from wowf.models.meta import Base


class Notification(Base):

    __tablename__ = 'notifications'
    __mapper_args__ = {'polymorphic_on': 'notification_type_id'}
    id = Column(Integer(unsigned=True), primary_key=True)
    notification_type_id = Column(
        Integer(unsigned=True), ForeignKey('notification_types.id', ondelete='cascade'),
        nullable=False)
    created_at = Column(DateTime, nullable=False, default=current_timestamp)

    users = relationship(
        'User', backref=backref('notifications', lazy='dynamic'),
        secondary='users_notifications')

    def __unicode__(self):
        return self.message

    def add_recipients(self, users):
        for user in users:
            if user not in self.users:
                self.users.append(user)


class _Notification(object):

    @declared_attr
    def id(cls):
        return Column(
            Integer(unsigned=True), ForeignKey('notifications.id', ondelete='cascade'),
            primary_key=True)


class RequestedChallengeNotification(_Notification, Notification):

    __tablename__ = 'requested_challenge_notifications'
    __mapper_args__ = {'polymorphic_identity': NotificationType.lookup_data.index('requested_challenge') + 1}
    user_id = Column(Integer(unsigned=True), ForeignKey('users.id', ondelete='cascade'), nullable=False)
    challenge_id = Column(Integer(unsigned=True), ForeignKey('challenges.id', ondelete='cascade'), nullable=False)

    user = relationship('User', lazy='joined')
    challenge = relationship('Challenge', lazy='joined')

    @property
    def message(self):
        request = get_current_request()
        user = link_to(self.user,
            url=request.route_url('user.view.challenges', id=self.user.id))
        challenge = link_to(self.challenge,
            url=request.route_url('challenge.view', id=self.challenge.id))
        return '%(user)s has challenged you to a %(challenge)s.' % dict(user=user, challenge=challenge)


class AcceptedChallengeNotification(_Notification, Notification):

    __tablename__ = 'accepted_challenge_notifications'
    __mapper_args__ = {'polymorphic_identity': NotificationType.lookup_data.index('accepted_challenge') + 1}
    user_id = Column(Integer(unsigned=True), ForeignKey('users.id', ondelete='cascade'), nullable=False)
    challenge_id = Column(Integer(unsigned=True), ForeignKey('challenges.id', ondelete='cascade'), nullable=False)

    user = relationship('User', lazy='joined')
    challenge = relationship('Challenge', lazy='joined')

    @property
    def message(self):
        request = get_current_request()
        user = link_to(self.user,
            url=request.route_url('user.view.challenges', id=self.user.id))
        challenge = link_to(self.challenge,
            url=request.route_url('challenge.view', id=self.challenge.id))
        return '%(user)s has accepted your %(challenge)s.' % dict(user=user, challenge=challenge)


class DeniedChallengeNotification(_Notification, Notification):

    __tablename__ = 'denied_challenge_notifications'
    __mapper_args__ = {'polymorphic_identity': NotificationType.lookup_data.index('denied_challenge') + 1}
    user_id = Column(Integer(unsigned=True), ForeignKey('users.id', ondelete='cascade'), nullable=False)
    challenge_id = Column(Integer(unsigned=True), ForeignKey('challenges.id', ondelete='cascade'), nullable=False)

    user = relationship('User', lazy='joined')
    challenge = relationship('Challenge', lazy='joined')

    @property
    def message(self):
        request = get_current_request()
        user = link_to(self.user,
            url=request.route_url('user.view.challenges', id=self.user.id))
        challenge = link_to(self.challenge,
            url=request.route_url('challenge.view', id=self.challenge.id))
        return '%(user)s has denied your %(challenge)s.' % dict(user=user, challenge=challenge)

class NewBuddyNotification(_Notification, Notification):

    __tablename__ = 'new_buddy_notifications'
    __mapper_args__ = {'polymorphic_identity': NotificationType.lookup_data.index('new_buddy') + 1}
    user_id = Column(Integer(unsigned=True), ForeignKey('users.id', ondelete='cascade'), nullable=False)

    user = relationship('User', lazy='joined')

    @property
    def message(self):
        request = get_current_request()
        user = link_to(self.user,
            url=request.route_url('user.view.challenges', id=self.user.id))
        return '%(user)s has added you as a buddy.' % dict(user=user)


class UploadedWorkoutNotification(_Notification, Notification):

    __tablename__ = 'uploaded_workout_notifications'
    __mapper_args__ = {'polymorphic_identity': NotificationType.lookup_data.index('uploaded_workout') + 1}
    user_id = Column(Integer(unsigned=True), ForeignKey('users.id', ondelete='cascade'), nullable=False)
    challenge_id = Column(Integer(unsigned=True), ForeignKey('challenges.id', ondelete='cascade'), nullable=False)

    user = relationship('User', lazy='joined')
    challenge = relationship('Challenge', lazy='joined')

    @property
    def message(self):
        request = get_current_request()
        user = link_to(self.user,
            url=request.route_url('user.view.challenges', id=self.user.id))
        challenge = link_to(self.challenge,
            url=request.route_url('challenge.view', id=self.challenge.id))
        return '%(user)s has completed the %(challenge)s.' % dict(user=user, challenge=challenge)