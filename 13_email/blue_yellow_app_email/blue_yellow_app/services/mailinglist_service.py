import mailchimp


class MailingListService:
    mailchimp_api = None
    mailchimp_list_id = None

    @staticmethod
    def global_init(api_key, list_id):
        MailingListService.mailchimp_api = api_key
        MailingListService.mailchimp_list_id = list_id

    @staticmethod
    def add_subscriber(email):
        if (MailingListService.mailchimp_api == 'ADD_YOUR_API_KEY' or
                    MailingListService.mailchimp_list_id == 'ADD_YOUR_LIST_ID'):
            print("WARNING: CANNOT USE MAILCHIMP API. KEYS NOT SET")
            print("Set your API keys in development.ini")
            return False

        api = mailchimp.Mailchimp(apikey=MailingListService.mailchimp_api)

        if not email or not email.strip():
            return False

        try:
            api.lists.subscribe(
                MailingListService.mailchimp_list_id,
                {'email': email.strip().lower()},
                double_optin=False,
                update_existing=True,
                replace_interests=False)
            return True
        except Exception as x:
            print("Error during mailing list signup: {}".format(x))
            return False
