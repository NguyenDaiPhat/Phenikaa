'''
Custom WTForms fields.
'''

from wowf.lib.widgets import EmailInput
from wtforms.fields import TextField


class EmailField(TextField):
    '''
    HTML5 email input type for email fields.
    '''

    widget = EmailInput()