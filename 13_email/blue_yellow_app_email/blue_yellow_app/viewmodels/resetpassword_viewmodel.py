from blue_yellow_app.services.account_service import AccountService
from blue_yellow_app.viewmodels.viewmodelbase import ViewModelBase


class ResetPasswordViewModel(ViewModelBase):
    def __init__(self):
        self.reset_code = None
        self.reset = None
        self.error_msg = None
        self.message = None
        self.password = None
        self.is_get = True

    def from_dict(self, data_dict):
        # reset_code will be third part of URL:
        #      /account/reset_password/f8489375729a
        # that is always id in our routing scheme
        self.reset_code = data_dict.get('id')

        self.password = data_dict.get('password')
        if self.reset_code:
            pass  # TODO: Get code from DB

    def validate(self):
        self.error_msg = None
        if not self.reset_code or not self.reset_code.strip():
            self.error_msg = "Reset code not found"
            return

        if not self.is_get:
            if not (self.password or self.password.strip()):
                self.error_msg = 'You must enter a valid password'
                return
            if len(self.password) < 3:
                self.error_msg = 'You must enter a password with at least a few characters'
                return

        # TODO: Validate code has not expired
        # TODO: Validate code has not been used
