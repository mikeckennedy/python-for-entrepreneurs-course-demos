import blue_yellow_app
from blue_yellow_app.data.dbsession import DbSessionFactory


def main():
    blue_yellow_app.init_db(None)
    add_test_data()


def add_test_data():
    pass


if __name__ == '__main__':
    main()