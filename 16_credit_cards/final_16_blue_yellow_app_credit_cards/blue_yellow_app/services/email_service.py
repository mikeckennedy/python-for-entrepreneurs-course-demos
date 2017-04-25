import mailer
import html2text

from blue_yellow_app.email.template_paser import EmailTemplateParser


class EmailService:
    __smtp_username = None
    __smtp_password = None
    __smtp_server = None
    __smtp_port = None
    __is_debug_mode = False
    __from_address = 'Talk Python Demo <demo@talkpython.fm>'

    @staticmethod
    def global_init(username, password, server, port, is_debug):
        EmailService.__is_debug_mode = is_debug
        EmailService.__smtp_username = username
        EmailService.__smtp_password = password
        EmailService.__smtp_port = int(port)
        EmailService.__smtp_server = server

    @staticmethod
    def send_email(to_address, subject, html_body):
        try:
            smtp = EmailService.create_smtp_server()
            message = mailer.Message(
                From=EmailService.__from_address,
                To=to_address,
                charset='utf-8')
            message.Subject = subject
            message.Html = html_body
            message.Body = html2text.html2text(html_body)

            if not EmailService.__is_debug_mode:
                print("Sending message (live!)")
                smtp.send(message)
            else:
                print("Skipping send, email is in dev mode.")
        except Exception as x:
            print("Error sending mail: {}".format(x))

    @staticmethod
    def create_smtp_server():
        smtp = mailer.Mailer(
            host=EmailService.__smtp_server,
            port=EmailService.__smtp_port,
            usr=EmailService.__smtp_username,
            pwd=EmailService.__smtp_password,
            use_tls=True
        )

        return smtp

    @classmethod
    def send_welcome_email(cls, email):
        html_body = EmailTemplateParser.expand(
            EmailTemplateParser.welcome,
            {'email': email}
        )
        EmailService.send_email(email, 'Welcome to Blue Yellow Rockets', html_body)

    @classmethod
    def send_password_reset_email(cls, email, reset_id):

        html_body = EmailTemplateParser.expand(
            EmailTemplateParser.reset_password,
            {'reset_code': reset_id}
        )
        EmailService.send_email(email, 'Reset your password at Blue Yellow Rockets', html_body)
