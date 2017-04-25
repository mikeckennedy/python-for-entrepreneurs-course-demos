from blue_yellow_app.viewmodels.viewmodelbase import ViewModelBase


class ForgotPasswordViewModel(ViewModelBase):
    def __init__(self):
        self.email = None
        self.error = None

    def from_dict(self, data_dict):
        self.email = data_dict.get('email')

    def validate(self):
        self.error = None
        if not self.email or not self.email.strip():
            self.error = "You must specify an email address"
            return
