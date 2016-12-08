import pyramid_handlers
from blue_yellow_app.controllers.base_controller import BaseController


class NewsletterController(BaseController):
    # POST /newsletter/add_subscriber
    @pyramid_handlers.action(request_method='POST')
    def add_subscriber(self):
        # todo: add to mailchimp

        # redirect
        self.redirect('/newsletter/subscribed')

    @pyramid_handlers.action(renderer='templates/newsletter/subscribed.pt')
    def subscribed(self):
        return {}

    @pyramid_handlers.action(renderer='templates/newsletter/failed.pt')
    def failed(self):
        return {}
