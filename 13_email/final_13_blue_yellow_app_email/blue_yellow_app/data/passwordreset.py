import datetime
import uuid

import sqlalchemy

from blue_yellow_app.data.modelbase import SqlAlchemyBase


class PasswordReset(SqlAlchemyBase):
    __tablename__ = 'PasswordReset'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True,
                           default=lambda: str(uuid.uuid4()).replace('-', ''))
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    used_date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=True)
    was_used = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    used_ip_address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    user_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('Account.id'))
