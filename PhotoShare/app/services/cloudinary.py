import hashlib

import cloudinary
import cloudinary.uploader

from PhotoShare.app.core.config import settings


class CloudinaryService:

    cloudinary.config(
        cloud_name=settings.cloudinary_name,
        api_key=settings.cloudinary_api_key,
        api_secret=settings.cloudinary_api_secret,
        secure=True
    )

    @staticmethod
    def get_public_id(filename: str) -> str:
        """
        Функція get_public_id приймає назву файлу як аргумент і повертає public_id.
        Public_id використовується для ідентифікації зображення в базі даних Cloudinary.
        Він створюється шляхом хешування назви файлу за допомогою SHA256 із використанням лише 10 символів цього хешу.
        Args:
        filename: str: Передача назву файлу зображення, яке завантажується
        Returns:
        str: Рядок із назвою файлу
        """
        public_id = hashlib.sha256(filename.encode()).hexdigest()[:10]
        return f"avatars/{public_id}"

    @staticmethod
    def upload_avater(file, public_id):
        """
        Функція upload_avatar приймає вибраний файл для завантаження  і  його public_id.
        Завантажу файл на cloudinary
        Args:
        file: Передача файлу зображення, яке завантажується
        Returns:
        Відповідь cloudinary після завантаження файлу
        """
        image = cloudinary.uploader.upload(file, public_id=public_id)
        return image

    @staticmethod
    def get_avatar_url(public_id: str, version: str) -> str:
        """
        Функція get_vatar_url будує посилання на зиінений завантажений користувацький аватар
        Args:
        public_id: str: Передача public_id зображення, яке вже завантажили
        version: str: Отримуємо version завантаженої аватарки
        Returns:
        Посилання на модіфікований аватар
        """
        url = cloudinary.CloudinaryImage(public_id).build_url(width=250, height=250, crop='fill', version=version)
        return url
