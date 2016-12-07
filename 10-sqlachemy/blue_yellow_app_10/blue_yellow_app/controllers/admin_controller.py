import pyramid_handlers
from blue_yellow_app.controllers.base_controller import BaseController
from blue_yellow_app.viewmodels.newalbumviewmodel import NewAlbumViewModel
from blue_yellow_app.viewmodels.register_viewmodel import RegisterViewModel


class AccountController(BaseController):
    # GET /admin/new_album
    @pyramid_handlers.action(renderer='templates/admin/new_album.pt',
                             request_method='GET',
                             name='new_album')
    def new_album_get(self):
        vm = NewAlbumViewModel()
        return vm.to_dict()

    # POST /account/register
    @pyramid_handlers.action(renderer='templates/admin/new_album.pt',
                             request_method='POST',
                             name='new_album')
    def new_album_post(self):
        vm = NewAlbumViewModel()
        vm.from_dict(self.request.POST)

        # might want to add this ;)
        # if not vm.validate():
        #     return vm.to_dict()

        # TODO: Create album in DB

        # redirect
        self.redirect('/albums')
