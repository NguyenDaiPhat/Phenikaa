'''
Pagination related functionality.
'''

from pyramid.threadlocal import get_current_request
from webhelpers.paginate import Page as _Page


DEFAULT_LIMIT = 20


def _get_url(page):
    request = get_current_request()
    _query = dict(request.GET)
    _query['page'] = page
    return request.current_route_url(_query=_query)


class Page(_Page):

    def __init__(self, collection, count, limit, **kwargs):
        '''
        @param collection A callable which returns a collection of items
        @param count A callable which returns the total number of items in the collection
        @param limit The max number of items to return
        @param kwargs Arguments to pass the collection callable.
        '''
        request = get_current_request()
        try:
            page = int(request.GET.get('page', 1))
        except ValueError:
            page = 1
        if callable(collection):
            collection = collection(limit=limit, page=page, **kwargs)
        if callable(count):
            count = count(**kwargs)
        super(Page, self).__init__(
            collection, item_count=count, items_per_page=limit, page=page,
            presliced_list=True, url=_get_url)


class Pager(object):
    '''
    Utility class to calculate pagination offset from page and limit.
    '''

    def __init__(self, page, limit):
        try:
            page = int(page)
        except Exception:
            page = 1

        try:
            limit = int(limit)
        except Exception:
            limit = DEFAULT_LIMIT

        self.page = max(page, 1)
        self.limit = max(limit, 1)
        self.offset = limit * (self.page - 1)