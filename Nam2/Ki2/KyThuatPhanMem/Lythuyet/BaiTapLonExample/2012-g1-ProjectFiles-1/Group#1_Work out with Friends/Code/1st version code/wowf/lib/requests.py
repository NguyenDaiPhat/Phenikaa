'''
Custom pyramid request objects.
'''

from beaker.cache import CacheManager
from pyramid.decorator import reify
from pyramid.request import Request
from wowf.lib.auth import Auth


class RequestFactory(Request):

    @reify
    def user(self):
        '''
        Return the currently logged in user.
        '''
        return Auth.get_current_user()

    @property
    def cache(self):
        '''
        Return a beaker cache object for quick and dirty caching.
        '''
        if not hasattr(self, '_cache'):
            self._cache = CacheManager()
        return self._cache