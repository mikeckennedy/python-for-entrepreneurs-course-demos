from pyramid.view import view_config
import designable_web.utils


@view_config(route_name='index', renderer='templates/index.pt')
def index(_):
    return extend_model({'project': 'designable_web'})


@view_config(route_name='box', renderer='templates/box_model.pt')
def box_model(_):
    return extend_model({})


@view_config(route_name='selectors', renderer='templates/selectors.pt')
def selectors(_):
    return extend_model({})


@view_config(route_name='layout', renderer='templates/layout.pt')
def layout(_):
    return extend_model({})


@view_config(route_name='float', renderer='templates/float.pt')
def float_(_):
    return extend_model({})


def extend_model(model_dict):
    model_dict['build_cache_id'] = designable_web.utils.build_cache_id
    return model_dict
