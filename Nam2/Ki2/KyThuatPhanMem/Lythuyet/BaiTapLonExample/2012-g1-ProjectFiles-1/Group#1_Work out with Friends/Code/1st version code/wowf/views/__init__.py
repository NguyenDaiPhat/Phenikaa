from wowf.config import settings
from wowf.lib import consts
from wowf.lib.pagination import Page


def get_challenge_stream(user):
    return Page(user.get_challenges,
                user.count_challenges,
                settings.max_stream_items)


def get_buddies_stream(user):
    return Page(user.get_buddies,
                user.count_buddies,
                settings.max_stream_items)


def get_unconfirmed_notification_stream(user):
    return Page(user.get_unconfirmed_notifications,
                user.count_unconfirmed_notifications,
                settings.max_stream_items)


def get_all_notification_stream(user):
    return Page(user.get_all_notifications,
                user.count_all_notifications,
                settings.max_stream_items)


class BaseView(object):

    def __init__(self, request):
        self.request = request
        self.settings = settings
        self.consts = consts