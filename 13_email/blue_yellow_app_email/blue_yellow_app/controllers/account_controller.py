import pyramid_handlers
from blue_yellow_app.controllers.base_controller import BaseController
from blue_yellow_app.services.account_service import AccountService
from blue_yellow_app.services.email_service import EmailService
from blue_yellow_app.viewmodels.forgotpassword_viewmodel import ForgotPasswordViewModel
from blue_yellow_app.viewmodels.register_viewmodel import RegisterViewModel
from blue_yellow_app.viewmodels.resetpassword_viewmodel import ResetPasswordViewModel
from blue_yellow_app.viewmodels.signin_viewmodel import SigninViewModel
import blue_yellow_app.infrastructure.cookie_auth as cookie_auth


class AccountController(BaseController):
    @pyramid_handlers.action(renderer='templates/account/index.pt')
    def index(self):
        if not self.logged_in_user_id:
            print("Cannot view account page, must login")
            self.redirect('/account/signin')

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

        cookie_auth.set_auth(self.request, account.id)

        return self.redirect('/account')

    @pyramid_handlers.action()
    def logout(self):
        cookie_auth.logout(self.request)
        self.redirect('/')

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
        cookie_auth.set_auth(self.request, account.id)

        # send welcome email
        EmailService.send_welcome_email(account.email)

        # redirect
        print("Redirecting to account index page...")
        self.redirect('/account')

    # Form to generate reset code, trigger email (get)
    @pyramid_handlers.action(renderer='templates/account/forgot_password.pt',
                             request_method='GET',
                             name='forgot_password')
    def forgot_password_get(self):
        vm = ForgotPasswordViewModel()
        return vm.to_dict()

    # Form to generate reset code, trigger email (post)
    @pyramid_handlers.action(renderer='templates/account/forgot_password.pt',
                             request_method='POST',
                             name='forgot_password')
    def forgot_password_post(self):
        vm = ForgotPasswordViewModel()
        vm.from_dict(self.data_dict)

        vm.validate()
        if vm.error:
            return vm.to_dict()

        reset = AccountService.create_reset_code(vm.email)
        if not reset:
            vm.error = 'Cannot find the account with that email.'
            return vm.to_dict()

        EmailService.send_password_reset_email(vm.email, reset.id)
        print("Would email the code {} to {}".format(
            reset.id, vm.email
        ))

        self.redirect('/account/reset_sent')

    # Form to actually enter the new password based on reset code (get)
    @pyramid_handlers.action(renderer='templates/account/reset_password.pt',
                             request_method='GET',
                             name='reset_password')
    def reset_password_get(self):
        vm = ResetPasswordViewModel()
        vm.from_dict(self.data_dict)
        vm.validate()
        return vm.to_dict()

    # Form to actually enter the new password based on reset code (post)
    @pyramid_handlers.action(renderer='templates/account/reset_password.pt',
                             request_method='POST',
                             name='reset_password')
    def reset_password_post(self):
        vm = ResetPasswordViewModel()
        vm.from_dict(self.data_dict)
        vm.is_get = False

        vm.validate()
        if vm.error_msg:
            return vm.to_dict()

        AccountService.use_reset_code(vm.reset_code, self.request.remote_addr)
        account = AccountService.find_account_by_id(vm.reset.user_id)
        AccountService.set_password(vm.password, account.id)

        vm.message = 'Your password has been reset, please login.'
        return vm.to_dict()

    # A reset has been sent via email
    @pyramid_handlers.action(renderer='templates/account/reset_sent.pt')
    def reset_sent(self):
        return {}
