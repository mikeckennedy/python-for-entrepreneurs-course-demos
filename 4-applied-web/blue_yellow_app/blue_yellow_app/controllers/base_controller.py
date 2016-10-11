import blue_yellow_app.infrastructure.static_cache as static_cache
from blue_yellow_app.infrastructure.supressor import suppress


class BaseController:
    def __init__(self, request):
        self.request = request
        self.build_cache_id = static_cache.build_cache_id

    @property
    def is_logged_in(self):
        return False

    @suppress
    def dont_expose_as_web_action_base(self):
        print("Called dont_expose_as_web_action on base, what happened?")
