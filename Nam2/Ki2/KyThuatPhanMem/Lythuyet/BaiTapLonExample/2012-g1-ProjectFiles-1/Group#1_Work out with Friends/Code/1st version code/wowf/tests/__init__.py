from pyramid import testing
from pyramid.paster import get_appsettings
from unittest import TestCase
from wowf.config import globalize_settings
from wowf.models import DBSession, initialize_db


settings = get_appsettings('development.ini')
settings['sqlalchemy.url'] = 'sqlite:///:memory:'

# Some features rely on global settings
globalize_settings(settings)


class BaseUnitTestCase(TestCase):

    def setUp(self):
        self.config = testing.setUp()
        initialize_db(settings)
        self.setup_db()

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def setup_db(self):
        pass