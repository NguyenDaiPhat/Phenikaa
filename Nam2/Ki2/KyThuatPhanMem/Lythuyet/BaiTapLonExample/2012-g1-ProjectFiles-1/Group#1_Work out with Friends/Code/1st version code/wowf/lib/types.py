'''
Custom SQLAlchemy types.
'''

import json
from sqlalchemy.types import TypeDecorator, Unicode


class JSONString(TypeDecorator):
    
    impl = Unicode
    
    def process_bind_param(self, value, dialect):
        if value is not None:
            value = unicode(json.dumps(value))
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value