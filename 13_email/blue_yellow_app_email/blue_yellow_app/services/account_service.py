from passlib.handlers.sha2_crypt import sha512_crypt
from blue_yellow_app.data.account import Account
from blue_yellow_app.data.dbsession import DbSessionFactory


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
