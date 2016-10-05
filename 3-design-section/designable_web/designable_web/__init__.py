from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('index', '/')
    config.add_route('box', '/box-model')
    config.add_route('selectors', '/selectors')
    config.add_route('layout', '/layout')
    config.add_route('float', '/float')
    config.scan()
    return config.make_wsgi_app()
