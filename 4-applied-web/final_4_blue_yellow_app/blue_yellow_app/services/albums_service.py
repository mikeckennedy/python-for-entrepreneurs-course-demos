class AlbumsService:
    @staticmethod
    def get_albums():
        return [
            {
                'title': 'Digital age boys and girls',
                'year': 2001,
                'has_preview': True,
                'image': '/static/img/albums/digital_album.jpg',
                'tracks': [
                    {'duration': '0:48', 'title': 'Welcome to the millennium'},
                    {'duration': '4:20', 'title': 'Renegade coders'},
                    {'duration': '5:01', 'title': 'Cyberpunks unite!'},
                    {'duration': '3:21', 'title': "We're all moving the Silicon Valley"},
                    {'duration': '2:22', 'title': "Tomorrow's people"},
                    {'duration': '4:24', 'title': 'I thought you were a robot'}
                ],
                'url': 'digital-age-boys-and-girls'
            },
            {
                'title': 'Year of the snake',
                'year': 1991,
                'has_preview': False,
                'image': '/static/img/albums/snake_album.jpg',
                'tracks': [
                    {'duration': '3:02', 'title': "Code like it's 1999"},
                    {'duration': '2:40', 'title': "Dawn of the iterators"},
                    {'duration': '5:21', 'title': "Running with descriptors"},
                    {'duration': '2:01', 'title': "Rage against the compilers"},
                    {'duration': '4:41', 'title': "Another line in the program"}
                ],
                'url': 'year-of-the-snake'
            }
        ]
