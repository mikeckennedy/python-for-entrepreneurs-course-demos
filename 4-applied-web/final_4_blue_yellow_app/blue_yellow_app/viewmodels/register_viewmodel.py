from blue_yellow_app.viewmodels.viewmodelbase import ViewModelBase


class RegisterViewModel(ViewModelBase):
    def __init__(self):
        self.email = None
        self.password = None
        self.confirm_password = None
        self.error = None

    def from_dict(self, data_dict):
        self.email = data_dict.get('email')
        self.password = data_dict.get('password')
        self.confirm_password = data_dict.get('confirm_password')

    def validate(self):
        self.error = None
        if self.password != self.confirm_password:
            self.error = "The password and confirmation don't match"
            return

        if not self.password:
            self.error = "You must specify a password"
            return

        if not self.email:
            self.error = "You must specify an email address"
            return
