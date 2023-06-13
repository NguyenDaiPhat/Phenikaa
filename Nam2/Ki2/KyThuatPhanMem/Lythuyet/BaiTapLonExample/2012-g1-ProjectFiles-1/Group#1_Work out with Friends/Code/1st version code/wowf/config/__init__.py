'''
Global access to configuration settings.

In order for it to work, the settings must be set on startup through the
globalize function. After that, settings can be used globally by importing
the settings object directly.
'''

from pyramid.settings import asbool
from wowf.lib.utils import Storage, settings_from_prefix


BOOLS = ('t', 'f', 'true', 'false', 'on', 'off')


def globalize_settings(config):
    settings.update(config)


class Settings(Storage):
    '''
    Storage container for settings, which attempts to guess the type, e.g., 
    number, boolean, etc. and convert accordingly.
    '''

    def __getitem__(self, key):
        value = super(Settings, self).__getitem__(key)
        if value.lower() in BOOLS:
            return asbool(value)
        if value.isdigit():
            return int(value)
        return value

    def from_prefix(self, prefix):
        return settings_from_prefix(self, prefix)


settings = Settings()