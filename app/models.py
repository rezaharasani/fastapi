from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('NOW()'))
    owner_id = Column(Integer, ForeignKey(
        'users.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    owner = relationship("User")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('NOW()'))
    phone_number = Column(String(11), nullable=False, unique=True)


class Vote(Base):
    __tablename__ = "votes"

    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE', onupdate='CASCADE'),
                     primary_key=True, nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id', ondelete='CASCADE', onupdate='CASCADE'),
                     primary_key=True, nullable=False)
