import datetime

from passlib.handlers.sha2_crypt import sha512_crypt
from blue_yellow_app.data.account import Account
from blue_yellow_app.data.dbsession import DbSessionFactory
from blue_yellow_app.data.passwordreset import PasswordReset


class AccountService:
    @staticmethod
    def create_account(email, plain_text_password):
        session = DbSessionFactory.create_session()

        account = Account()
        account.email = email
        account.password_hash = AccountService.hash_text(plain_text_password)

        session.add(account)
        session.commit()

        return account

    @classmethod
    def find_account_by_email(cls, email):

        if not email or not email.strip():
            return None

        email = email.lower().strip()

        session = DbSessionFactory.create_session()

        account = session.query(Account) \
            .filter(Account.email == email) \
            .first()

        return account

    @staticmethod
    def hash_text(plain_text_password):
        hashed_text = sha512_crypt.encrypt(plain_text_password, rounds=150000)
        return hashed_text

    @classmethod
    def get_authenticated_account(cls, email, plain_text_password):
        account = AccountService.find_account_by_email(email)
        if not account:
            return None

        if not sha512_crypt.verify(plain_text_password, account.password_hash):
            return None

        return account

    @classmethod
    def find_account_by_id(cls, user_id):
        if not user_id:
            return None

        session = DbSessionFactory.create_session()

        account = session.query(Account) \
            .filter(Account.id == user_id) \
            .first()

        return account

    @staticmethod
    def create_reset_code(email):

        account = AccountService.find_account_by_email(email)
        if not account:
            return None

        session = DbSessionFactory.create_session()

        reset = PasswordReset()
        reset.used_ip_address = '1.2.3.4'  # set for real
        reset.user_id = account.id

        session.add(reset)
        session.commit()

        return reset

    @classmethod
    def find_reset_code(cls, code):

        if not code or not code.strip():
            return None

        session = DbSessionFactory.create_session()
        reset = session.query(PasswordReset).\
            filter(PasswordReset.id == code).\
            first()

        return reset

    @classmethod
    def use_reset_code(cls, reset_code, user_ip):
        session = DbSessionFactory.create_session()

        reset = session.query(PasswordReset). \
            filter(PasswordReset.id == reset_code). \
            first()

        if not reset:
            return

        reset.used_ip_address = user_ip
        reset.was_used = True
        reset.used_date = datetime.datetime.now()

        session.commit()

    @classmethod
    def set_password(cls, plain_text_password, account_id):
        print('Resetting password for user {}'.format(account_id))
        session = DbSessionFactory.create_session()

        account = session.query(Account). \
            filter(Account.id == account_id). \
            first()

        if not account:
            print("Warning: Cannot reset password, no account found.")
            return

        print("New password set.")
        account.password_hash = AccountService.hash_text(plain_text_password)
        session.commit()
