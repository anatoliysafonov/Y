import hashlib

import cloudinary
import cloudinary.uploader
from fastapi import APIRouter, Depends, status, UploadFile, File
from sqlalchemy.orm import Session

from PhotoShare.app.models.user import User
from PhotoShare.app.services.auth_service import get_current_user
from PhotoShare.app.schemas.user import UserRespond, UserFirstname, UserLastname
from PhotoShare.app.core.database import get_db
from PhotoShare.app.repositories.users import update_user

router_user = APIRouter(prefix="/user", tags=["user"])


@router_user.get("/profile", response_model=UserRespond, status_code=status.HTTP_200_OK,
                 summary='Отримати інформацію про користувача')
async def me(user: User = Depends(get_current_user)):
    return user


@router_user.patch("/edit/username/{username}", response_model=UserRespond, status_code=status.HTTP_200_OK)
async def change_username(username: str, user: User = Depends(get_current_user), session: Session = Depends(get_db)):
    user.username = username
    user = await update_user(user, session)
    return user


@router_user.patch("/edit/firstname/{firstname}", response_model=UserRespond, status_code=status.HTTP_200_OK)
async def edit_firstname(body: UserFirstname, user: User = Depends(get_current_user),
                         session: Session = Depends(get_db)):
    user.first_name = body.first_name
    user = await update_user(user, session)
    return user


@router_user.patch("/edit/lastname/{lastname}", response_model=UserRespond, status_code=status.HTTP_200_OK)
async def edit_lastname(body: UserLastname, user: User = Depends(get_current_user),
                        session: Session = Depends(get_db)):
    user.last_name = body.last_name
    user = await update_user(user, session)
    return user


@router_user.patch("/edit/avatar", response_model=UserRespond, status_code=status.HTTP_200_OK)
async def upload_avatar(file: UploadFile = File(), user: User = Depends(get_current_user),
                        session: Session = Depends(get_db)):
    cloudinary.config(
        cloud_name="dojm1hfxr",
        api_key="224227453225525",
        api_secret="kJ9D2rxqqmdRT9T_VhEbo6EpUvs",
        # cloud_name="demnd161p",
        # api_key="387793814646383",
        # api_secret="wdF9CRgOI99GFvYVYZ_-keQ_yzw",
        secure=True,
    )
    public_id = f"Y/{user.email}/avatar/" + hashlib.sha256(file.filename.encode()).hexdigest()[:10]
    image = cloudinary.uploader.upload(file.file, public_id=public_id, overwrite=True)
    url = cloudinary.CloudinaryImage(public_id).build_url(width=250, height=250, crop='fill',
                                                          version=image.get('version'))
    user.avatar = url
    user = await update_user(user, session)
    return user


