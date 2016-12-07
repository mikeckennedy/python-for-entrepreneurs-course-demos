from pyramid.config import Configurator
import os
import blue_yellow_app
import blue_yellow_app.controllers.home_controller as home
import blue_yellow_app.controllers.albums_controller as albums
import blue_yellow_app.controllers.account_controller as account
import blue_yellow_app.controllers.admin_controller as admin
from blue_yellow_app.data.dbsession import DbSessionFactory


def init_db(config):
    top_folder = os.path.dirname(blue_yellow_app.__file__)
    rel_folder = os.path.join('db', 'blue_yellow.sqlite')

    db_file = os.path.join(top_folder, rel_folder)
    DbSessionFactory.global_init(db_file)


def main(_, **settings):
    config = Configurator(settings=settings)

    init_includes(config)
    init_routing(config)
    init_db(config)

    return config.make_wsgi_app()


def init_routing(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_handler('root', '/', handler=home.HomeController, action='index')

    add_controller_routes(config, home.HomeController, 'home')
    add_controller_routes(config, albums.AlbumsController, 'albums')
    add_controller_routes(config, account.AccountController, 'account')
    add_controller_routes(config, admin.AdminController, 'admin')

    config.scan()


def add_controller_routes(config, ctrl, prefix):
    config.add_handler(prefix + 'ctrl_index', '/' + prefix, handler=ctrl, action='index')
    config.add_handler(prefix + 'ctrl_index/', '/' + prefix + '/', handler=ctrl, action='index')
    config.add_handler(prefix + 'ctrl', '/' + prefix + '/{action}', handler=ctrl)
    config.add_handler(prefix + 'ctrl/', '/' + prefix + '/{action}/', handler=ctrl)
    config.add_handler(prefix + 'ctrl_id', '/' + prefix + '/{action}/{id}', handler=ctrl)


def init_includes(config):
    config.include('pyramid_chameleon')
    config.include('pyramid_handlers')
