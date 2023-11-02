import re

from Bot.handlers.base_handlers import handler_get_photo
from Bot.lexicon.lexicon import LEXICON_roles, LEXICON, LEXICON_admin
from Bot.commands.base_command import vk, base_func
from Bot.models.methods import add_admin_method
from Bot.services.services import create_or_update_photo, set_state
from Bot.state_machine.state_machine import ADMIN, ADD_ADMIN, CHANGE_PHOTO, CHECK_PHOTO, MENU
from Bot.keyboards.keyboards import admin_menu_kb, base_kb, change_photo_kb, roles


def handler_admin_role(user_id):
    """Меню админа"""
    request = base_func(user_id, LEXICON_roles['admin'], admin_menu_kb)  # клавиатура и ответ
    set_state(user_id, ADMIN)  # устанавливаем состояние пользователя
    return request


def handler_not_admin_or_unknown(user_id):
    """Пользователь не админ или неизвестная команда"""
    request = base_func(user_id, LEXICON['no_admin_or_unknown'], roles)  # клавиатура и ответ
    set_state(user_id, MENU)  # устанавливаем состояние пользователя
    return request


def handler_how_to_add_admin(user_id):
    """Как добавить админа"""
    request = base_func(user_id, LEXICON_admin['how_to_add_admin'], base_kb)  # клавиатура и ответ
    set_state(user_id, ADD_ADMIN)  # устанавливаем состояние пользователя

    return request


def handler_add_admin(event, user_id):
    """Логика добавления админа"""
    user = None
    # получаем id админа по одному из шаблонов
    if re.search(r'https://vk\.com/[a-zA-Z0-9]{5,32}', event.message['text']):
        user = vk.users.get(user_ids=event.message['text'].split('/')[-1])
    elif re.search('[a-zA-Z0-9]{5,32}', event.message['text']):
        user = vk.users.get(user_ids=event.message['text'])

    if not user:  # не верный шаблон добавление админа
        return handler_add_admin_template_error(user_id)

    message = LEXICON_admin['admin_added']  # получаем сообщение
    admin = add_admin_method(user[0]['id'])  # добавляем админа в базу
    if not admin:  # если админ в базе
        message = LEXICON_admin['admin_in_base']  # получаем сообщение
    request = base_func(user_id, message, base_kb)  # клавиатура и ответ

    set_state(user_id, ADD_ADMIN)  # устанавливаем состояние пользователя
    return request


def handler_add_admin_template_error(user_id):
    """Ошибка шаблона для добавления админа """
    request = base_func(user_id, LEXICON_admin['error_admin_template'], base_kb)  # клавиатура и ответ
    set_state(user_id, ADD_ADMIN)  # устанавливаем состояние пользователя
    return request


def handler_replace_photo(event, user_id):
    """Изменяем выбранное фото"""

    # получаем url самого большого фото
    photo_url = event.message['attachments'][0]['photo']['sizes'][3]['url']

    # создаём или обновляем фото
    answer = create_or_update_photo(photo_url, user_id)

    message = LEXICON_admin['photo_added']  # получаем сообщение
    if not answer:  # если какое-то фото уже было в базе
        message = LEXICON_admin['photo_update']  # получаем сообщение

    request = base_func(user_id, message, change_photo_kb)  # клавиатура и ответ
    set_state(user_id, CHECK_PHOTO)  # устанавливаем состояние пользователя
    return request


def handler_write_photo(event, user_id):
    """Отправляем выбранное фото и ожидаем новое"""
    request = base_func(user_id, LEXICON_admin['add_photo'], base_kb)  # клавиатура и ответ
    handler_get_photo(event, user_id)  # получаем фото для отправки и отправляем
    set_state(user_id, CHANGE_PHOTO)  # устанавливаем состояние пользователя
    return request


def handler_check_photo(user_id):
    request = base_func(user_id, LEXICON_admin['check_photo'], change_photo_kb)  # клавиатура и ответ
    set_state(user_id, CHECK_PHOTO)  # устанавливаем состояние пользователя
    return request


def handler_error_replace_photo(user_id):
    request = base_func(user_id, LEXICON_admin['error_replace_photo'], base_kb)  # клавиатура и ответ
    set_state(user_id, CHANGE_PHOTO)  # устанавливаем состояние пользователя
    return request
