import os
import requests

from Bot.lexicon.lexicon import LEXICON_photo_name
from Bot.models.methods import replace_photo_method, check_photo
from Bot.state_machine.state_machine import *

PATH = os.path.dirname(__file__)  # текущая директория
TWO_FOLDER_UP = os.path.abspath(os.path.join(PATH, '../../ktep_vk'))  # директория проекта
CURR_PATH = os.path.join(TWO_FOLDER_UP, 'images')  # директория images


def create_or_update_photo(photo_url, user_id):
    """Создаём или обновляем путь и само фото"""
    response = requests.get(photo_url).content  # получаем фото от вк

    with open(photo_url.split('/')[-1].split('?')[0], 'wb') as f:  # открываем файл на запись
        f.write(response)  # записываем содержимое фото
        filename = f.name  # получаем имя фото

    curr_photo = get_state_and_photo(user_id)  # получаем текущее фото
    after_path = os.path.join(TWO_FOLDER_UP, filename)  # изначально фото хранится в главной директории
    before_path = os.path.join(CURR_PATH, curr_photo['curr_photo'], filename)  # путь, куда будем загружать фото
    folder_path = os.path.dirname(before_path)  # путь к папке с нужным фото
    db_photo_path = os.path.join(curr_photo['curr_photo'], filename)  # получаем полный путь к нужному фото

    if not os.path.exists(folder_path):  # если директории нет
        os.makedirs(folder_path)  # создаём

    os.rename(after_path, before_path)  # загружаем фото в нужную директорию

    answer = replace_photo_method(curr_photo['curr_photo'], db_photo_path) # обновляем или добавляем данные о фото в бд

    return answer


def get_write_photo(event, upload, user_id):
    """Загружаем фото на сервер вк и устанавливаем состояние текущего фото"""
    image = None
    # Ищем название нужной директории с фото
    for key, value in LEXICON_photo_name.items():
        if value == event.message['text']:
            image = key

    path_to_photo = _get_path_photo(image) # получаем путь к фото
    photo = upload.photo_messages(path_to_photo)  # загружаем фото на сервер вк
    set_photo(user_id, image)  # обновляем состояние фото
    return photo


def _get_path_photo(image):
    """Получаем путь к фото"""
    path = check_photo(image)  # есть ли фото в бд
    if path:  # возвращаем путь к фото
        image_path = path.image_path
        path_to_photo = os.path.join(CURR_PATH, image_path)
    else: # возвращаем путь к фото по умолчанию
        path_to_photo = os.path.join(CURR_PATH, 'default.png')

    return path_to_photo


def register_user(user_id):
    """Создаём пользователя в бд"""
    redis_client.hset(user_id, mapping={
        'state': START,
        'curr_photo': ''
    })


def set_state(user_id, state):
    """Устанавливаем состояние"""
    redis_client.hset(user_id, 'state', state)


def set_photo(user_id, curr_photo):
    """Устанавливаем текущее фото"""
    redis_client.hset(user_id, 'curr_photo', curr_photo)


def get_state_and_photo(user_id):
    """Возвращаем данные о пользователе"""
    data = redis_client.hgetall(user_id)
    return data
