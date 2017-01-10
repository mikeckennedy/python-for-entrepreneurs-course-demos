from blue_yellow_app.data.account import Account
from blue_yellow_app.data.album import Album
from blue_yellow_app.data.dbsession import DbSessionFactory


class StoreService:
    @staticmethod
    def purchase_album(user: Account, album: Album,
                       amount_paid: float, stripe_token: str):
        # TODO: ...
        pass

    @staticmethod
    def __record_purchase(user_id: int, album_id: int,
                          amount_paid: float, description: str):
        session = DbSessionFactory.create_session()
        # TODO: ...

    @staticmethod
    def get_purchased_album_ids(user_id: int):
        session = DbSessionFactory.create_session()
        # TODO: ...
