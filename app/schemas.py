from datetime import datetime
from typing import Optional, Annotated
from pydantic import BaseModel, EmailStr, conint, BeforeValidator, Field, ConfigDict
from app import utils


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    phone_number: str = Field(min_length=11, max_length=11)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    phone_number: Annotated[str, BeforeValidator(utils.reformat_phone_number)]

    model_config = ConfigDict(from_attributes=True)


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    model_config = ConfigDict(from_attributes=True)


class PostOut(BaseModel):
    Post: Post
    votes: int

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
