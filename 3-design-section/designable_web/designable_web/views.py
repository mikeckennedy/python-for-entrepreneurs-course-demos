from pyramid.view import view_config


@view_config(route_name='index', renderer='templates/index.pt')
def index(_):
    return extend_model({'project': 'designable_web'})


@view_config(route_name='box', renderer='templates/box-model.pt')
def box_model(_):
    return extend_model({})


@view_config(route_name='selectors', renderer='templates/selectors.pt')
def selectors(_):
    return extend_model({})


@view_config(route_name='grid', renderer='templates/grid_layouts.pt')
def grid_layouts(_):
    return extend_model({})


def extend_model(model_dict):
    return model_dict
