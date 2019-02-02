import pyramid_handlers
from blue_yellow_app.controllers.base_controller import BaseController
from blue_yellow_app.services.mailinglist_service import MailingListService


class NewsletterController(BaseController):
    # POST /newsletter/add_subscriber
    @pyramid_handlers.action(request_method='POST')
    def add_subscriber(self):
        # Let's just make this seem to work on the live site
        # Of course, we don't really run a website for Blue Rockets Band
        # They are fictional :)

        # email = self.data_dict.get('email')
        # if MailingListService.add_subscriber(email):
        #     self.redirect('/newsletter/subscribed')
        #
        # self.redirect('/newsletter/failed')

        self.redirect('/newsletter/subscribed')

    @pyramid_handlers.action(renderer='templates/newsletter/subscribed.pt')
    def subscribed(self):
        return {}

    @pyramid_handlers.action(renderer='templates/newsletter/failed.pt')
    def failed(self):
        return {}
