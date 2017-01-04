from blue_yellow_app.viewmodels.viewmodelbase import ViewModelBase


class ResetPasswordViewModel(ViewModelBase):
    def __init__(self):
        self.reset_code = None
        self.error_msg = None
        self.message = None
        self.password = None
        self.is_get = True

    def from_dict(self, data_dict):
        self.reset_code = data_dict.get('reset_code')
        self.password = data_dict.get('password')
        if self.reset_code:
            pass  # TODO: Get code from DB

    def validate(self):
        self.error_msg = None
        if not self.reset_code or not self.reset_code.strip():
            self.error_msg = "Reset code not found"
            return

        # TODO: Validate code has not expired
        # TODO: Validate code has not been used
