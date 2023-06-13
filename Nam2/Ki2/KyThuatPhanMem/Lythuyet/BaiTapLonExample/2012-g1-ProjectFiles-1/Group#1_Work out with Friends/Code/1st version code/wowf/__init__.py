import os
import time
from pyramid.authentication import SessionAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator
from pyramid_beaker import session_factory_from_settings, set_cache_regions_from_settings
from wowf.config import globalize_settings, routes
from wowf.lib.predicates import LoggedIn, RequestMethod, RouteName
from wowf.lib.requests import RequestFactory
from wowf.lib.resources import RootFactory
from wowf.models import initialize_sqla


def main(global_config, **settings):
    '''
    Configure and return a WSGI application.
    '''
    globalize_settings(settings)
    initialize_sqla(settings)
    set_cache_regions_from_settings(settings)
    config = Configurator(
        settings=settings,
        request_factory=RequestFactory,
        root_factory=RootFactory,
        authentication_policy=SessionAuthenticationPolicy(),
        authorization_policy=ACLAuthorizationPolicy(),
        session_factory=session_factory_from_settings(settings))
    config.include('pyramid_jinja2')
    config.include('pyramid_mailer')
    config.include('pyramid_rewrite')
    config.include('pyramid_tm')
    config.include(routes)
    config.add_renderer('.html', 'pyramid_jinja2.renderer_factory')
    config.add_static_view(settings['static_url'], 'wowf:static')
    config.add_static_view(settings['avatar_url'], settings['avatar_dir'])
    config.add_view_predicate('logged_in', LoggedIn)
    config.add_subscriber_predicate('route_name', RouteName)
    config.add_subscriber_predicate('request_method', RequestMethod)
    config.scan('wowf.views')
    config.scan('wowf.lib.subscribers')
    os.environ['TZ'] = settings['timezone']
    time.tzset()
    return config.make_wsgi_app()