'''
Route configuration.
'''

def includeme(config):
    config.add_route('home', '/')
    config.add_route('user.login', '/login')
    config.add_route('user.logout', '/logout')
    config.add_route('user.register', '/register')
    config.add_route('user.notifications.unconfirmed', '/notifications')
    config.add_route('user.notifications.all', '/notifications/all')
    config.add_route('user.view.challenges', '/user/{id:\d+}')
    config.add_route('user.view.buddies', '/user/{id:\d+}/buddies')
    config.add_route('user.invite', '/invite')
    config.add_route('challenge.create', '/challenge/create')
    config.add_route('challenge.create.speed', '/challenge/create/speed')
    config.add_route('challenge.create.endurance', '/challenge/create/endurance')
    config.add_route('challenge.create.bench', '/challenge/create/bench')
    config.add_route('challenge.create.squat', '/challenge/create/squat')
    config.add_route('challenge.view', '/challenge/{id:\d+}')
    config.add_route('search.users', '/search')
    config.add_route('account.profile', '/account')
    config.add_route('account.password', '/account/password')
    config.add_route('account.password.request', '/account/password/reset')
    config.add_route('account.password.reset', '/account/password/reset/{token}')
    config.add_rewrite_rule('/favicon.ico', '/static/favicon.ico')
    config.add_rewrite_rule('/robots.txt', '/static/robots.txt')
    config.add_rewrite_rule('/sitemap.xml', '/static/sitemap.xml')
    config.add_rewrite_rule('/dublin.rdf', '/static/dublin.rdf')