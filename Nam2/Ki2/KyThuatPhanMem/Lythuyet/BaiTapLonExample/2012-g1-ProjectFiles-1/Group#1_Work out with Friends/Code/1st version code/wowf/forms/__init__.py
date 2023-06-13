from wowf.lib.utils import Storage
from wtforms import Form as _Form


class State(Storage):
    '''
    Storage object to pass state to forms for more complex validation.
    '''
    pass


class Form(_Form):
    '''
    Updated form object, which accepts a state variable to assist in more complex
    validation.
    '''

    def __init__(self, formdata=None, obj=None, prefix='', state=None, **kwargs):
        super(Form, self).__init__(formdata, obj, prefix, **kwargs)
        if not state:
            state = State()
        self.state = state


from wowf.forms.challenge import *
from wowf.forms.search import *
from wowf.forms.user import *
from wowf.forms.workout import *