import pyramid_handlers
from blue_yellow_app.controllers.base_controller import BaseController
from blue_yellow_app.services.store_service import StoreService


class StoreController(BaseController):
    @pyramid_handlers.action(renderer='templates/store/complete.pt')
    def complete(self):
        return {}

    @pyramid_handlers.action(renderer='templates/store/success.pt')
    def success(self):
        return {}

    @pyramid_handlers.action(renderer='templates/store/failed.pt')
    def failed(self):
        return {}
