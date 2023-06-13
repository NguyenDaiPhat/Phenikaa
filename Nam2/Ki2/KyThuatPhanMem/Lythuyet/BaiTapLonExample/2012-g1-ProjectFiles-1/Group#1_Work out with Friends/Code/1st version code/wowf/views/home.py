from pyramid.view import view_config, view_defaults
from wowf.views import BaseView


@view_defaults(route_name='home', permission='guest', logged_in=False)
class HomeView(BaseView):

    @view_config(renderer='home.html')
    def main(self):
        return dict()


@view_defaults(route_name='home', permission='member', logged_in=True)
class DashboardView(BaseView):

    @view_config(renderer='dashboard.html')
    def main(self):
        stream = self.request.user.get_challenges(self.settings.min_stream_items)
        return dict(stream=stream)