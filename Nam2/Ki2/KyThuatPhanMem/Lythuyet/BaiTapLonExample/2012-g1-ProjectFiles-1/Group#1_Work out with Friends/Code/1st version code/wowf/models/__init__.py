from sqlalchemy.engine import engine_from_config
from wowf.lib.fulltext import initialize_fulltext
from wowf.models.challenge import *
from wowf.models.lookup_tables import *
from wowf.models.meta import *
from wowf.models.notification import *
from wowf.models.pivot_tables import *
from wowf.models.tokens import *
from wowf.models.user import *
from wowf.models.workout import *


def initialize_sqla(settings):
    '''
    Initialize the SQLAlchemy connections.
    '''
    initialize_fulltext(settings)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine


def initialize_db(settings):
    '''
    Initialize the SQLAlchemy database.
    '''
    initialize_sqla(settings)
    Base.metadata.create_all()
    populate_lookups()