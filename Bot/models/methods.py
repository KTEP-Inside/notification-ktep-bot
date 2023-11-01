from Bot.models.models import *

db.connect()


def add_admin_method(admin):
    """Добавляем или возвращаем id админа"""
    admin, created = AdminModel.get_or_create(admin_id=admin)
    return created


def check_admin(admin):
    """Проверка на админа"""
    admin = AdminModel.get_or_none(admin_id=admin)
    return admin


def check_photo(image_name):
    """Проверка на наличие фото в бд"""
    photo = ImageModel.get_or_none(image_name=image_name)
    return photo


def replace_photo_method(image_name, image_path):
    """должен обновлять выбранное фото, работаем через путь из бд"""
    photo = ImageModel.get_or_none(image_name=image_name)
    if photo is None:  # если фото нет в бд
        ImageModel.create(image_name=image_name, image_path=image_path)
        return True
    else:  # если есть
        photo.image_path = image_path
        photo.save()
        return False


db.close()