from __future__ import unicode_literals
import datetime
from wowf.models import Buddy, Challenge, Notification, SpeedChallenge, User
from wowf.models.pivot_tables import UserChallenge
from wowf.tests import BaseUnitTestCase


class BaseModelTestCase(BaseUnitTestCase):

    def setup_db(self):
        User.__table__.insert().execute([
            dict(id=1, username='MarkSmith', email='mark@gmail.com', password='password',
                 gender='M', dob=datetime.datetime(year=1980, month=1, day=1),
                 weight=80, height=1.65),
            dict(id=2, username='LeslieJames', email='leslie@yahoo.com', password='password',
                 gender='F', dob=datetime.datetime(year=1985, month=7, day=7),
                 weight=60, height=1.6),
            dict(id=3, username='JustinJones', email='justin@msn.com', password='password',
                 gender='M', dob=datetime.datetime(year=1990, month=5, day=5),
                 weight=70, height=1.7),
        ])
        Buddy.__table__.insert().execute([
            dict(user_id=1, buddy_id=2),
            dict(user_id=3, buddy_id=1),
        ])
        Challenge.__table__.insert().execute([
            dict(id=1, user_id=1, challenge_type_id=1),
            dict(id=2, user_id=3, challenge_type_id=1),
        ])
        SpeedChallenge.__table__.insert().execute([
            dict(id=1, distance=100),
            dict(id=2, distance=100),
        ])
        UserChallenge.__table__.insert().execute([
            dict(user_id=1, challenge_id=1, is_accepted=True),
            dict(user_id=2, challenge_id=1, is_accepted=None),
            dict(user_id=3, challenge_id=2, is_accepted=True),
            dict(user_id=1, challenge_id=2, is_accepted=False),
        ])


class UserModelTestCase(BaseModelTestCase):

    def test_create_user(self):
        data = dict(
            username='MaryJane', email='maryj@gmail.com', password='mary90210',
            gender='M', dob=datetime.datetime(year=1989, month=7, day=23),
            weight=81.6466, height=1.778)
        user = User.create(**data)
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, data['email'])
        self.assertNotEqual(user.password, data['password'])
        self.assertTrue(user.is_active)
        self.assertIsNotNone(user.id)
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.last_active_at)

    def test_get_by_id(self):
        id = 1
        user = User.get_by_id(id)
        self.assertIsInstance(user, User)
        self.assertEqual(user.id, id)
        id = 999
        user = User.get_by_id(id)
        self.assertIsNone(user)

    def test_get_by_email(self):
        email = 'mark@gmail.com'
        user = User.get_by_email(email)
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, email)
        user = User.get_by_email('doesnotexist@email.com')
        self.assertIsNone(user)

    def test_is_buddy(self):
        user = User.get_by_id(2)
        buddy = User.get_by_id(1)
        self.assertTrue(user.is_buddy(buddy))
        stranger = User.get_by_id(3)
        self.assertFalse(user.is_buddy(stranger))

    def test_add_buddy(self):
        user = User.get_by_id(2)
        stranger = User.get_by_id(3)
        self.assertFalse(user.is_buddy(stranger))
        user.add_buddy(stranger)
        self.assertTrue(user.is_buddy(stranger))

    def test_remove_buddy(self):
        user = User.get_by_id(1)
        buddy = User.get_by_id(2)
        self.assertTrue(user.is_buddy(buddy))
        user.remove_buddy(buddy)
        self.assertFalse(user.is_buddy(buddy))

    def test_get_buddies(self):
        user = User.get_by_id(1)
        expected_user_ids = (2, 3)
        buddies = user.get_buddies()
        self.assertEqual(len(buddies), len(expected_user_ids))
        for user in buddies:
            self.assertIsInstance(user, User)
            self.assertIn(user.id, expected_user_ids)

    def test_get_challenges(self):
        user = User.get_by_id(1)
        expected_challenge_ids = (1, 2)
        challenges = user.get_challenges()
        self.assertEqual(len(challenges), len(expected_challenge_ids))
        for challenge in challenges:
            self.assertIsInstance(challenge, Challenge)
            self.assertIn(challenge.id, expected_challenge_ids)

    def test_in_challenge(self):
        user = User.get_by_id(1)
        challenge = Challenge.get_by_id(1)
        self.assertTrue(user.in_challenge(challenge))
        user = User.get_by_id(3)
        self.assertFalse(user.in_challenge(challenge))

    def test_owns_challenge(self):
        user = User.get_by_id(1)
        challenge = Challenge.get_by_id(1)
        self.assertTrue(user.owns_challenge(challenge))
        user = User.get_by_id(2)
        self.assertFalse(user.owns_challenge(challenge))

    def test_accept_challenge(self):
        creator = User.get_by_id(1)
        competitor = User.get_by_id(2)
        challenge = Challenge.get_by_id(1)
        self.assertFalse(competitor.accepted_challenge(challenge))
        self.assertEqual(creator.count_unconfirmed_notifications(), 0)
        competitor.accept_challenge(challenge)
        self.assertTrue(competitor.accepted_challenge(challenge))
        self.assertEqual(creator.count_unconfirmed_notifications(), 1)
        for notification in creator.get_all_notifications():
            self.assertIsInstance(notification, Notification)
            self.assertIsInstance(notification.user, User)
            self.assertIsNotNone(notification.user.id)
            self.assertIsInstance(notification.challenge, Challenge)
            self.assertIsNotNone(notification.challenge.id)

    def test_deny_challenge(self):
        creator = User.get_by_id(1)
        competitor = User.get_by_id(2)
        challenge = Challenge.get_by_id(1)
        self.assertFalse(competitor.denied_challenge(challenge))
        self.assertEqual(creator.count_unconfirmed_notifications(), 0)
        competitor.deny_challenge(challenge)
        self.assertTrue(competitor.denied_challenge(challenge))
        self.assertEqual(creator.count_unconfirmed_notifications(), 1)

    def test_create_speed_challenge(self):
        creator = User.get_by_id(1)
        competitor = User.get_by_id(2)
        distance = 400
        self.assertEqual(competitor.count_unconfirmed_notifications(), 0)
        creator.create_speed_challenge(competitor, distance)
        self.assertEqual(competitor.count_unconfirmed_notifications(), 1)


class SpeedChallengeModelTestCase(BaseModelTestCase):

    def test_create_challenge(self):
        user = User.get_by_id(1)
        distance = 100 # meters
        challenge = SpeedChallenge.create(user, distance)
        self.assertIsInstance(challenge, SpeedChallenge)
        self.assertEqual(challenge.distance, distance)
        self.assertEqual(challenge.creator, user)