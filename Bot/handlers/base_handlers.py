from Bot.lexicon.lexicon import LEXICON
from Bot.commands.base_command import *
from Bot.services.services import get_write_photo, register_user, set_state
from Bot.keyboards.keyboards import roles
from Bot.state_machine.state_machine import MENU


def handler_start(user_id):
    """Начать"""
    request = base_func(user_id, LEXICON['your_role'], roles)  # клавиатура и ответ
    register_user(user_id)  # Регистрируем пользователя в бд
    set_state(user_id, MENU)  # устанавливаем состояние пользователя
    return request


def handler_get_photo(event, user_id):
    """Получаем нужное фото и отправляем"""
    photo = get_write_photo(event, upload, user_id)  # получаем и загружаем нужное фото
    photo_data = photo[0]  # забираем данные об id photo
    send_photo(user_id, url=f'photo{photo_data["owner_id"]}_{photo_data["id"]}')  # отправляем фото
