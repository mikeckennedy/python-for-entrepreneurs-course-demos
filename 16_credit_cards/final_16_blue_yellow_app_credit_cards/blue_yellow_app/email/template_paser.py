import os


class EmailTemplateParser:
    welcome = None
    reset_password = None

    @staticmethod
    def global_init():
        templates = os.path.join(
            os.path.dirname(__file__),
            'templates'
        )
        welcome_file = os.path.join(templates, 'welcome.html')
        with open(welcome_file) as fin:
            EmailTemplateParser.welcome = fin.read()

        welcome_file = os.path.join(templates, 'password_reset.html')
        with open(welcome_file) as fin:
            EmailTemplateParser.reset_password = fin.read()

    @staticmethod
    def expand(template, data):

        final_text = template
        for k in data:
            key = '{' + k + '}'
            final_text = final_text.replace(key, data[k])

        return final_text
