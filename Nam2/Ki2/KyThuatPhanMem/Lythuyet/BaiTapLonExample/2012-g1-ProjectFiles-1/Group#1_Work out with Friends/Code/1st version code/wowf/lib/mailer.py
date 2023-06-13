'''
Email specific helper functions.
'''

from pyramid.renderers import render
from pyramid.settings import aslist
from pyramid.threadlocal import get_current_request
from pyramid_mailer import get_mailer
from pyramid_mailer.message import Message


def send_mail(subject, recipients, template, variables=None, extra_headers=None, attachments=None, sender=None):
    '''
    Send an email to the given recipients.

    @param template Path to email template
    @param variables Dictionary of variables to pass to the template
    @param attachments Files to attach to the email
    @param sender Email address of sender, if not the default sender
    '''
    recipients = aslist(recipients)
    if variables is None:
        variables = {}
    if attachments is not None and not isinstance(attachments, list):
        attachments = [attachments]
    request = get_current_request()
    mailer = get_mailer(request)
    html = render(template, variables, request)
    message = Message(
        subject=subject, bcc=recipients, html=html, extra_headers=extra_headers,
        attachments=attachments, sender=sender)
    mailer.send(message)