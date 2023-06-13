from __future__ import unicode_literals
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from wowf.lib.fulltext import FulltextBase
from zope.sqlalchemy import ZopeTransactionExtension


DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))


class Base(FulltextBase):

    query = DBSession.query_property()

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __repr__(self):
        return repr(unicode(self))

    def __unicode__(self):
        return self.__class__.__name__

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        DBSession.add(obj)
        DBSession.flush()
        return obj

    def delete(self):
        DBSession.delete(self)


Base = declarative_base(cls=Base)