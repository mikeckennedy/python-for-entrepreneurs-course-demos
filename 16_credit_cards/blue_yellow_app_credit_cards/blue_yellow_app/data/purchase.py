import datetime


import sqlalchemy
import sqlalchemy.orm
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from blue_yellow_app.data.modelbase import SqlAlchemyBase


class AlbumPurchase(SqlAlchemyBase):
    __tablename__ = 'AlbumPurchase'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, default=datetime.datetime.now, index=True)

    description = Column(String)
    amount_paid = sqlalchemy.Column(sqlalchemy.Float, index=True)

    album_id = Column(String, ForeignKey('Album.id'))
    user_id = Column(String, ForeignKey('Account.id'))
