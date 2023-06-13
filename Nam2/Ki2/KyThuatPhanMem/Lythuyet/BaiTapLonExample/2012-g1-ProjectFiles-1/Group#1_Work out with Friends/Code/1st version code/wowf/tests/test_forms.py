from __future__ import unicode_literals
from wowf.tests import BaseUnitTestCase


class BaseFormTestCase(BaseUnitTestCase):

    Form = None
    invalid_data = []
    valid_data = []

    def setup_db(self):
        pass

    def test_validation(self):
        for data in self.invalid_data:
            form = self.Form(**data)
            self.assertFalse(form.validate())
        for data in self.valid_data:
            form = self.Form(**data)
            self.assertTrue(form.validate())