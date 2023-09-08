from datetime import datetime

from pydantic import BaseModel, EmailStr


class BaseUserModel(BaseModel):
    email: EmailStr = 'user@gmail.com'
    password: str = 'qwerty'

class UserLoginModel(BaseUserModel):
    ...

class UserRegisterModel(BaseUserModel):
    username: str
    first_name: str
    last_name: str

class UserProfileModel(BaseUserModel):
    first_name: str | None
    last_name: str | None
    created_at: datetime
    avatar: str
    uploaded_photos: int


class UserRespond(BaseModel):
    id: int
    email: EmailStr
    username: str | None
    first_name: str | None
    last_name: str | None
    uploaded_photos: int
    avatar: str
    role: str

    class Config:                                                                                                # noqa
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class UserUsername(BaseModel):
    username: str


class UserFirstname(BaseModel):
    first_name: str


class UserLastname(BaseModel):
    last_name: str
