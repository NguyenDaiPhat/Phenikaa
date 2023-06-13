'''
Helpers to assist in Whoosh fulltext indexing and searching.
'''

from __future__ import unicode_literals
import os
from whoosh.analysis import NgramFilter, StandardAnalyzer
from whoosh.fields import ID, SchemaClass, TEXT
from whoosh.filedb.filestore import FileStorage, RamStorage
from whoosh.index import exists_in
from whoosh.qparser import QueryParser


index = None
parser = QueryParser
analyzer = StandardAnalyzer() | NgramFilter(minsize=2, maxsize=2)


def initialize_fulltext(settings):
    global index
    index_path = settings.get('fulltext_dir')
    if not index_path:
        storage = RamStorage()
        index = storage.create_index(schema=WhooshSchema)
        return
    if not os.path.exists(index_path):
        os.makedirs(index_path)
    storage = FileStorage(index_path)
    if not exists_in(index_path):
        index = storage.create_index(schema=WhooshSchema)
    else:
        index = storage.open_index(schema=WhooshSchema)


class WhooshSchema(SchemaClass):
    '''
    Very generic indexing schema.
    '''

    index_id = ID(stored=True, unique=True)
    data = TEXT(stored=False, analyzer=analyzer)


class FulltextBase(object):
    '''
    Adds support for fulltext searching to SQLAlchemy's Base object.
    '''

    index_fields = []

    @classmethod
    def index_type(cls):
        return cls.__name__

    def index_id(self):
        return '%s:%s' % (self.index_type(), self.id)

    def index_data(self):
        return ' '.join([unicode(getattr(self, attr)) for attr in self.index_fields])

    def add_index(self, writer):
        '''
        Add a fulltext index for this instance.
        '''
        if self.index_fields:
            writer.add_document(index_id=self.index_id(), data=self.index_data())

    def delete_index(self, writer):
        '''
        Delete the fulltext index for this instance.
        '''
        if self.index_fields:
            writer.delete_by_term('index_id', self.index_id())

    def update_index(self, writer):
        '''
        Update the fulltext index for this instance.
        '''
        if self.index_fields:
            writer.update_document(index_id=self.index_id(), data=self.index_data())

    @classmethod
    def _get_fulltext_query(cls, terms):
        '''
        Return a query for items after performing a fulltext search.
        '''
        ids = _search(terms, cls.index_type())
        return cls.query.filter(cls.id.in_(ids))


def _search(terms, index_type):
    '''
    Perform a search of the given type using the terms. Return all ids which
    match.
    '''
    query = parser('data', index.schema).parse(terms)
    with index.searcher() as searcher:
        results = searcher.search(query)
        ids = _results_to_ids(results, index_type)
    return ids


def _results_to_ids(results, index_type):
    '''
    Convert search results to ids to be used in a SQLAlchemy query.
    '''
    ids = set()
    for result in results:
        type, id = result.get('index_id').split(':')
        if type == index_type:
            ids.add(id)
    return ids