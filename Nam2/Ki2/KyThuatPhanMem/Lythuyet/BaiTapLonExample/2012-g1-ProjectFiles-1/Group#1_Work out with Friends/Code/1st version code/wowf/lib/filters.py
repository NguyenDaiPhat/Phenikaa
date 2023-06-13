'''
Custom Jinja2 template filters.
'''

import itertools
import pretty
from webhelpers import text
from wowf.lib.utils import to_user_timezone


def datetimeformat(value, format='%I:%M %p on %b %d', timezone=None):
    '''
    Format the given datetime according to the given format.

    @param value datetime instance
    @param timezone Timezone to convert to before rendering
    '''
    if timezone:
        value = to_user_timezone(value, timezone)
    return value.strftime(format)


def timesince(value, asdays=False, short=True):
    '''
    Show the elapsed time since the given datetime.

    @param value datetime instance
    '''
    return pretty.date(value, asdays, short)


def pluralize(value, singular, plural, with_number=True):
    '''
    @param value Number of items
    @param singular Singular form of items
    @param plural Plural form of items
    '''
    return text.plural(value, singular, plural, with_number)


def groupbydate(value):
    '''
    Group items by date.
    '''
    return itertools.groupby(value,
        lambda item: (item.created_at.year, item.created_at.month, item.created_at.day))