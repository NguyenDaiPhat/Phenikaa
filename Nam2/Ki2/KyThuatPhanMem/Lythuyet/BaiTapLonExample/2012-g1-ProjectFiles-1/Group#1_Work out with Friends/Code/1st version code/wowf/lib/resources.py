'''
Custom pyramid resources.
'''

from pyramid.security import Allow, Authenticated, Deny, Everyone


class RootFactory(object):

    __acl__ = [(Allow, Authenticated, 'member'),
               (Deny, Authenticated, 'guest'),
               (Allow, Everyone, 'guest')]

    def __init__(self, request):
        pass