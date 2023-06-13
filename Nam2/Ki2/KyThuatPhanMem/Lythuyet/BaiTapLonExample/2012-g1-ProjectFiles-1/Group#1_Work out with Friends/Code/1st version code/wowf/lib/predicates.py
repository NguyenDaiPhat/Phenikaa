'''
Custom pyramid predicates.
'''

import re


class BasePredicate(object):

    def __init__(self, value, config):
        self.value = value
        self.config = config

    def text(self):
        argname = self.__class__.__name__
        argname = (argname[0].lower() +
                   re.sub(r'([A-Z])', lambda m: '_' + m.group(0).lower(), argname[1:]))
        return '%s = %s' % (argname, self.value)
    phash = text


class LoggedIn(BasePredicate):
    '''
    View predicate to check whether user is logged in.
    '''

    def __call__(self, context, request):
        logged_in = bool(request.user)
        return logged_in == self.value


class RouteName(BasePredicate):
    '''
    Context found subscriber predicate to check against route name.
    '''

    def __call__(self, event):
        route_name = event.request.matched_route.name
        return route_name == self.value


class RequestMethod(BasePredicate):
    '''
    Context found subscriber predicate to check against request method.
    '''

    def __call__(self, event):
        request_method = event.request.method
        return request_method == self.value