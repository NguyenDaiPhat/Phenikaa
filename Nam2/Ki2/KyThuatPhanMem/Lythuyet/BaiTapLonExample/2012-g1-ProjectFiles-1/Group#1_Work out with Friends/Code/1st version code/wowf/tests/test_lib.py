from __future__ import unicode_literals
import datetime
from wowf.lib.auth import Auth
from wowf.lib.pagination import Pager
from wowf.lib.utils import (
    Storage, calculate_bmi, parse_timedelta, to_system_timezone,
    to_user_timezone, years_ago)
from wowf.tests import BaseUnitTestCase


class AuthTestCase(BaseUnitTestCase):

    def test_hash_password(self):
        original = 'password'
        hashed = Auth.hash_password(original)
        self.assertNotEqual(original, hashed)
        self.assertEqual(hashed, Auth.hash_password(original, hashed))


class UtilsTestCase(BaseUnitTestCase):

    def test_years_ago(self):
        today = datetime.date.today()
        start = datetime.date(year=1980, month=1, day=1)
        self.assertEqual(years_ago(start), today.year - start.year)

    def test_calculate_bmi(self):
        weight = 45.3592
        height = 1.524
        self.assertEqual(calculate_bmi(weight, height), 19.5)

    def test_pager(self):
        self.assertEqual(Pager(1, 10).offset, 0)
        self.assertEqual(Pager(2, 10).offset, 10)
        self.assertEqual(Pager(1, None).offset, 0)
        self.assertEqual(Pager(None, 10).offset, 0)
        self.assertEqual(Pager(None, None).offset, 0)

    def test_to_timezone(self):
        timezone = 'America/New_York'
        original_dt = datetime.datetime(2012, 1, 1)
        offset = datetime.timedelta(hours=5) # Standard time, not DST
        user_dt = to_user_timezone(original_dt, timezone)
        self.assertEqual(original_dt.strftime('%s'), (user_dt + offset).strftime('%s'))

    def test_from_timezone(self):
        timezone = 'America/New_York'
        original_dt = datetime.datetime(2012, 1, 1)
        offset = datetime.timedelta(hours=5) # Standard time, not DST
        system_dt = to_system_timezone(original_dt, timezone)
        self.assertEqual(original_dt.strftime('%s'), (system_dt - offset).strftime('%s'))

    def test_parse_timedelta(self):
        td = parse_timedelta(datetime.timedelta(days=7, hours=12, minutes=30))
        self.assertEqual(td.days, 7)
        self.assertEqual(td.hours, 12)
        self.assertEqual(td.minutes, 30)
        td = parse_timedelta(datetime.timedelta(hours=36))
        self.assertEqual(td.days, 1)
        self.assertEqual(td.hours, 12)
        self.assertEqual(td.minutes, 0)

    def test_storage(self):
        bar = 'bar'
        storage = Storage(foo=bar)
        self.assertEqual(storage['foo'], bar)
        self.assertEqual(storage['foo'], storage.foo)
        self.assertRaises(AttributeError, storage.__getattr__, 'doesntexist')