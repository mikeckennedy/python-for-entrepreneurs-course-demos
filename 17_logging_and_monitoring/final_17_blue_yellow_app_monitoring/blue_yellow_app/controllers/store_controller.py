import pyramid_handlers

from blue_yellow_app.controllers.base_controller import BaseController
from blue_yellow_app.services.albums_service import AlbumsService
from blue_yellow_app.services.store_service import StoreService


class StoreController(BaseController):
    @pyramid_handlers.action()
    def complete(self):
        # {'stripeToken': 'tok_19aUhV4bdW93NdzOnsPOc8K4',
        # 'stripeTokenType': 'card',
        # 'stripeEmail': 'mikeckennedy@gmail.com',
        # 'action': 'complete',
        # 'id': 28}

        album_id = int(self.data_dict.get('id', -1))
        album = AlbumsService.get_album_by_id(album_id)

        token = self.data_dict.get('stripeToken')
        StoreService.purchase_album(self.logged_in_user, album, album.price, token)

        # TODO: send email receipt to self.data_dict['stripeEmail']
        self.log.notice("YAY, we have a purchase: {} bought {}".format(
            self.logged_in_user.email,
            album.name
        ))

        self.redirect('/store/success/{}'.format(album.id))

    @pyramid_handlers.action(renderer='templates/store/success.pt')
    def success(self):
        album_id = int(self.data_dict.get('id', -1))
        album = AlbumsService.get_album_by_id(album_id)
        return {'album': album}

    @pyramid_handlers.action(renderer='templates/store/failed.pt')
    def failed(self):
        return {}
