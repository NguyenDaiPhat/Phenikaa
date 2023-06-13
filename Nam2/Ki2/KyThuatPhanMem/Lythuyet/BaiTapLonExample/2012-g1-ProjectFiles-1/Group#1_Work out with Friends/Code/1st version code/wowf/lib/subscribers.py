'''
Application event subscribers.
'''

from __future__ import unicode_literals
import datetime
from jinja2 import Markup
from pyramid.events import BeforeRender, ContextFound, subscriber
from pyramid.httpexceptions import HTTPBadRequest
from pyramid.threadlocal import get_current_request
from random import choice
from sqlalchemy import event
from wowf.config import settings
from wowf.lib import consts
from wowf.lib.fulltext import index
from wowf.lib.utils import Storage
from wowf.models.meta import DBSession


@subscriber(ContextFound, request_method='POST')
def csrf_validation(event):
    '''
    Perform CSRF validation on all POST requests early in the request cycle.
    '''
    request = event.request
    token = request.POST.get('token')
    if token is None:
        raise HTTPBadRequest('CSRF token is missing')
    elif token != request.session.get_csrf_token():
        raise HTTPBadRequest('CSRF token is invalid')
        
        
@subscriber(BeforeRender)
def add_renderer_globals(event):
    '''
    Pass variables to the template.
    '''
    request = get_current_request()
    token = request.session.get_csrf_token()
    token_field = Markup('<input type="hidden" name="token" value="%s" />' % token)
    event['g'] = Storage(consts, settings=settings, token_field=token_field)
    event['h'] = Storage(datetime=datetime, choice=choice)


@event.listens_for(DBSession, 'after_flush')
def update_indexes(session, flush_context):
    '''
    Automatically add, update, and delete indexes as necessary.
    '''
    writer = index.writer()
    for obj in session.new:
        obj.add_index(writer)
    for obj in session.dirty:
        obj.update_index(writer)
    for obj in session.deleted:
        obj.delete_index(writer)
    writer.commit()