import pyramid_handlers
from blue_yellow_app.controllers.base_controller import BaseController
from blue_yellow_app.services.account_service import AccountService
from blue_yellow_app.viewmodels.register_viewmodel import RegisterViewModel
from blue_yellow_app.viewmodels.signin_viewmodel import SigninViewModel


class AccountController(BaseController):
    @pyramid_handlers.action(renderer='templates/account/index.pt')
    def index(self):
        return {}

    @pyramid_handlers.action(renderer='templates/account/signin.pt',
                             request_method='GET',
                             name='signin')
    def signin_get(self):
        return SigninViewModel().to_dict()

    @pyramid_handlers.action(renderer='templates/account/signin.pt',
                             request_method='POST',
                             name='signin')
    def signin_post(self):
        vm = SigninViewModel()
        vm.from_dict(self.data_dict)

        account = AccountService.get_authenticated_account(vm.email, vm.password)
        if not account:
            vm.error = "Email address or password are incorrect."
            return vm.to_dict()

        return self.redirect('/account')

    @pyramid_handlers.action(renderer='templates/account/register.pt',
                             request_method='GET',
                             name='register')
    def register_get(self):
        vm = RegisterViewModel()
        return vm.to_dict()

    @pyramid_handlers.action(renderer='templates/account/register.pt',
                             request_method='POST',
                             name='register')
    def register_post(self):
        vm = RegisterViewModel()
        vm.from_dict(self.request.POST)

        vm.validate()
        if vm.error:
            return vm.to_dict()

        account = AccountService.find_account_by_email(vm.email)
        if account:
            vm.error = "An account with this email already exists. " \
                       "Please log in instead."
            return vm.to_dict()

        account = AccountService.create_account(vm.email, vm.password)
        print("Registered new user: " + account.email)

        # send welcome email

        # redirect
        print("Redirecting to account index page...")
        self.redirect('/account')
