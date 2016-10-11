from pyramid.view import view_config
import blue_yellow_app.infrastructure.static_cache as static_cache


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {
        'project': 'blue_yellow_app',
        'build_cache_id': static_cache.build_cache_id
    }
