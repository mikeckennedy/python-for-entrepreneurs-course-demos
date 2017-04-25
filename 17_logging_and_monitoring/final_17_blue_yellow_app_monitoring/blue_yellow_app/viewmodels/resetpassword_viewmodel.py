import datetime

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
            self.reset = AccountService.find_reset_code(self.reset_code)

    def validate(self):
        self.error_msg = None
        if not self.reset:
            self.error_msg = "Reset code not found"
            return

        if not self.is_get:
            if not (self.password or self.password.strip()):
                self.error_msg = 'You must enter a valid password'
                return
            if len(self.password) < 3:
                self.error_msg = 'You must enter a password with at least a few characters'
                return

        if self.reset.was_used:
            self.error_msg = 'This reset code has already been used.'
            return

        if self.reset.was_used:
            self.error_msg = 'This reset code has already been used.'
            return

        dt = datetime.datetime.now() - self.reset.created_date
        days = dt.total_seconds() / 60 / 60 / 24
        if days > 1:
            self.error_msg = 'This reset code has expired, generate a new one.'
            return
