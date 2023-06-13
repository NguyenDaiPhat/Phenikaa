from __future__ import unicode_literals
import transaction
from sqlalchemy.orm import backref, relationship
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, Unicode
from wowf.lib.utils import get_subclasses
from wowf.models.meta import Base


def populate_lookups():
    '''
    Populate all lookup tables defined in this module.
    '''
    from wowf.models import lookup_tables
    transaction.begin()
    for cls in get_subclasses(lookup_tables, lookup_tables.Lookup):
        cls.populate()
    transaction.commit()


class Lookup(object):

    lookup_data = ()
    id = Column(Integer(unsigned=True), primary_key=True)
    name = Column(Unicode(40), nullable=False, index=True)

    def __init__(self, name):
        self.name = name

    def __unicode__(self):
        return self.name

    @classmethod
    def create(cls, name):
        return super(Lookup, cls).create(name=name)

    @classmethod
    def populate(cls):
        for name in cls.lookup_data:
            try:
                cls.get_by_name(name)
            except NoResultFound:
                cls.create(name)

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter(cls.name==name).one()


class NotificationType(Lookup, Base):

    __tablename__ = 'notification_types'
    lookup_data = (
        'requested_challenge', 'accepted_challenge', 'denied_challenge',
        'new_buddy', 'uploaded_workout')


class ChallengeType(Lookup, Base):

    __tablename__ = 'challenge_types'
    lookup_data = (
        'speed', 'endurance', 'bench_press', 'squat')


class Group(Lookup, Base):

    __tablename__ = 'groups'
    lookup_data = ('login', 'admin')

    users = relationship(
        'User', backref=backref('groups', lazy='dynamic'),
        secondary='users_groups', lazy='dynamic')