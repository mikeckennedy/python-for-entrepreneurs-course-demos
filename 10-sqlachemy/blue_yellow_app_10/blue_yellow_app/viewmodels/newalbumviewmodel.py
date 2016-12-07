from blue_yellow_app.viewmodels.viewmodelbase import ViewModelBase


class NewAlbumViewModel(ViewModelBase):
    def __init__(self):
        self.title = None
        self.year = None
        self.price = None
        self.album_image = None
        self.url = None
        self.tracks_text = None
        self.error = None

    def from_dict(self, data_dict):
        self.title = data_dict.get('title')
        self.year = int(data_dict.get('year'))
        self.price = float(data_dict.get('price'))
        self.album_image = data_dict.get('album_image')
        self.url = data_dict.get('url')
        self.tracks_text = data_dict.get('tracks_text')

    @property
    def track_titles(self):
        return [
            t.strip()
            for t in self.tracks_text.split('\n')
            if t and t.strip()
        ]

