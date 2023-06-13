'''
Custom WTForms widgets.
'''

from wtforms.widgets import Input


class EmailInput(Input):
    
    input_type = 'email'