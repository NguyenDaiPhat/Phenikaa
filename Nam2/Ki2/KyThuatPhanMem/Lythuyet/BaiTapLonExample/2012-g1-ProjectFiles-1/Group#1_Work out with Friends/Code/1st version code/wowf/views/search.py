from pyramid.view import view_config, view_defaults
from wowf.forms import SearchUserForm, State
from wowf.models import User
from wowf.views import BaseView


search_view_forms = {'search.users': SearchUserForm}


@view_defaults(route_name='search.users', permission='member')
class SearchView(BaseView):

    @view_config(renderer='search/users.html', permission='member')
    def main(self):
        form = search_view_forms[self.request.matched_route.name](self.request.GET, state=State(id=self.request.user.id))
        stream = None
        if 'q' in self.request.GET and form.validate():
            stream = form.search(self.settings.max_stream_items)
        return dict(form=form,
                    stream=stream)

    @view_config(renderer='json', xhr=True)
    def ajax(self):
        username = self.request.GET.get('username', '')
        users = set(User.search(username)) - set([self.request.user])
        if users:
            return [{'username': user.username, 'gender': user.gender, 'age': user.age,
                     'avatar': self.request.static_url(user.avatar.small)}
                    for user in users]