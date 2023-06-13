from __future__ import unicode_literals
from wowf.forms import Form
from wowf.lib.pagination import Page
from wowf.models import User
from wtforms.fields import TextField


class SearchForm(Form):

    q = TextField('Search')


class SearchUserForm(SearchForm):

    def search(self, limit=50):
        return Page(
            User.search, User.count_search_results,  limit, terms=self.q.data)