'''
Miscellaneous helper functions.
'''

import csv
import inspect
import math
import times
from datetime import date, datetime


TIMESTAMP = 'timestamp_epoch'
DISTANCE = 'DISTANCE'
HEARTRATE = 'HEARTRATE'
CALORIEBURN = 'CALORIEBURN'


def parse_workout_report(workout_report):
    '''
    Parse and extract the needed data from the csv of the workout report.
    '''
    csv_reader = csv.reader(workout_report)
    csv_header = None
    samples = {}
    try:
        while not csv_header:
            csv_header = csv_reader.next()
    except:
        return samples
    for row in csv_reader:
        try:
            samples.setdefault('timestamp', []).append(float(row[csv_header.index(TIMESTAMP)]))
            samples.setdefault('distance', []).append(float(row[csv_header.index(DISTANCE)]))
            samples.setdefault('heart_rate', []).append(float(row[csv_header.index(HEARTRATE)]))
            samples.setdefault('calories_burned', []).append(float(row[csv_header.index(CALORIEBURN)]))
        except:
            pass
    if samples['timestamp']:
        # Downshift timestamps
        leading_timestamp = samples['timestamp'][0]
        samples['timestamp'] = map(lambda x: x - leading_timestamp, samples['timestamp'])
    return samples


def calculate_wilks_coefficient(weight, gender):
    '''
    Calculate the wilkes coefficient for this user.

    @param weight The users weight (kg).
    '''
    x = weight
    if gender == 'M':
        a = -216.0475144
        b = 16.2606339
        c = -0.002388645
        d = -0.00113732
        e = 7.01863e-06
        f = -1.291e-08
    else:
        a = 594.31747775582
        b = -27.23842536447
        c = 0.82112226871
        d = -0.00930733913
        e = 0.00004731582
        f = -0.00000009054
    return 500.0 / (a + b * x + c * x**2 + d * x**3 + e * x**4 + f * x**5)


def calculate_one_rep_max(weight, repetitions):
    '''
    Calculate the estimated one rep max.

    @param weight How much weight the user lifted.
    @param repetitions How many times the user lifted the weight.
    '''
    w = weight
    r = repetitions
    return (100.0 * w) / (48.8 + 53.8 * math.exp(-0.075 * r))


def calculate_bmi(weight, height):
    '''
    Calculate a persons body mass index, given weight (kg) and height (m).
    '''
    try:
        return round(weight / (height ** 2), 1)
    except:
        return False


def years_ago(start_dt):
    '''
    Calculate the difference in years between the start date and today.
    '''
    today = date.today()
    if isinstance(start_dt, datetime):
        start_dt = start_dt.date()
    try:
        dt = start_dt.replace(year=today.year)
    except ValueError:
        # Start date is February 29 and the current year is not a leap year
        dt = start_dt.replace(year=today.year, day=start_dt.day-1)
    if dt > today:
        return today.year - start_dt.year - 1
    else:
        return today.year - start_dt.year


def get_subclasses(module, base, with_base=False):
    '''
    Get all classes residing in a given module which subclass a given base class.

    @param with_base Whether to include the base class also
    '''
    subclasses = []
    for name, cls in inspect.getmembers(module):
        if inspect.isclass(cls) and issubclass(cls, base):
            if not with_base and cls is base:
                continue
            subclasses.append(cls)
    return subclasses


def split_cslist(cslist):
    '''
    Split a comma separated list by both newlines and commas.
    '''
    items = []
    for line in cslist.splitlines():
        for item in line.split(','):
            item.strip() and items.append(item.strip())
    return items


def current_timestamp():
    return datetime.utcnow()


def to_user_timezone(dt, timezone):
    '''
    Convert a datetime from system timezone to the given timezone.
    '''
    from wowf.config import settings
    timezone = timezone or settings.timezone
    return times.to_local(dt, timezone)


def to_system_timezone(dt, timezone):
    '''
    Convert a datetime from the given timezone to system timezone.
    '''
    from wowf.config import settings
    timezone = timezone or settings.timezone
    return times.to_universal(dt, timezone)


def parse_timedelta(td):
    '''
    Get the days, hours, and minutes from a timedelta object.
    '''
    days, hours, minutes = td.days, td.seconds // 3600, (td.seconds // 60) % 60
    return Storage(days=days, hours=hours, minutes=minutes)


def settings_from_prefix(settings, prefix):
    '''
    Return a dictionary of settings all containing the same key prefix, with the
    prefix removed from the keys.
    '''
    data = {}
    for key in settings:
        if key.startswith(prefix):
            data[key.replace(prefix, '')] = settings[key]
    return data


class Storage(dict):
    '''
    Generic container class.
    '''

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as e:
            raise AttributeError(e)

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError as e:
            raise AttributeError(e)