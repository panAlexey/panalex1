import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin


class Plants(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'plants'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    animal = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    count = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=0)
    desc = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # noanimal = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # nick = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    countReg = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=0)
    users = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    # user = orm.relation("User")

    def __repr__(self):
        return f'<Totem> {self.animal}'
