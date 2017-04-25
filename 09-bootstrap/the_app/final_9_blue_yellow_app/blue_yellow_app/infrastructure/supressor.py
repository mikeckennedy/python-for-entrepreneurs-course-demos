import pyramid_handlers


# noinspection PyPep8Naming
class suppress(pyramid_handlers.action):
    def __init__(self, _, **kw):
        kw['request_method'] = 'NOT_A_HTTP_VERB'
        super().__init__(**kw)

