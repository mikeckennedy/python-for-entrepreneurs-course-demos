import pyramid_handlers
from blue_yellow_app.controllers.base_controller import BaseController


class AccountController(BaseController):
    @pyramid_handlers.action(renderer='templates/account/index.pt')
    def index(self):
        return {}

    @pyramid_handlers.action(renderer='templates/account/signin.pt')
    def signin(self):
        return {}

    # GET /account/register
    @pyramid_handlers.action(renderer='templates/account/register.pt',
                             request_method='GET',
                             name='register')
    def register_get(self):
        print("Calling register via GET...")
        return {
                'email': None,
                'password': None,
                'confirm_password': None,
                'error': None
            }

    # POST /account/register
    @pyramid_handlers.action(renderer='templates/account/register.pt',
                             request_method='POST',
                             name='register')
    def register_post(self):
        email = self.request.POST.get('email')
        pw = self.request.POST.get('password')
        pw_confirmation = self.request.POST.get('confirm_password')

        print("Calling register via POST: {}, {}, {}".format(email, pw, pw_confirmation))

        if pw != pw_confirmation:
            return {
                'email': email,
                'password': pw,
                'confirm_password': pw_confirmation,
                'error': "The password and confirmation don't match"
            }

        # validate no account exists, passwords match
        # create account in DB
        # send welcome email

        # redirect
        print("Redirecting to account index page...")
        self.redirect('/account')

