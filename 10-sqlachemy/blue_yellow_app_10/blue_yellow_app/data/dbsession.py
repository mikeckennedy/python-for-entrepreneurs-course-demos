import sqlalchemy
from blue_yellow_app.data.modelbase import SqlAlchemyBase
# noinspection PyUnresolvedReferences
import blue_yellow_app.data.album
# noinspection PyUnresolvedReferences
import blue_yellow_app.data.track


class DbSessionFactory:
    @staticmethod
    def global_init(db_file):
        if not db_file or not db_file.strip():
            raise Exception("You must specify a data file.")

        conn_str = 'sqlite:///' + db_file
        print("Connecting to db with conn string: {}".format(conn_str))

        engine = sqlalchemy.create_engine(conn_str)
        SqlAlchemyBase.metadata.create_all(engine)
