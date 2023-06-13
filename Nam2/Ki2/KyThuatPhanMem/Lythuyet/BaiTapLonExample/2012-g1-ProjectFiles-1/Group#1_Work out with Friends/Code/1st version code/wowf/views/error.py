from pyramid.httpexceptions import HTTPForbidden, HTTPFound, HTTPNotFound
from pyramid.view import view_config, view_defaults
from wowf.lib.auth import Auth
from wowf.views import BaseView


@view_defaults(context=HTTPForbidden)
class ForbiddenView(BaseView):

    @view_config()
    def main(self):
        headers = None
        if not self.request.user:
            headers = Auth.auto_login()
            if headers:
                location = self.request.url
            else:
                location = self.request.route_url('user.login', _query={'return_to': self.request.url})
        else:
            location = self.request.route_url('home')
        return HTTPFound(location=location, headers=headers)


@view_defaults(context=HTTPNotFound)
class NotFoundView(BaseView):

    @view_config(renderer='error/not_found.html')
    def main(self):
        return dict()


@view_defaults(context=Exception)
class CatchAllView(BaseView):

    @view_config(renderer='error/catch_all.html')
    def main(self):
        if self.settings.debug:
            raise
        return dict()