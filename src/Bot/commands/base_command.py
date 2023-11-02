from vk_api.utils import get_random_id
# не убирать, прокидывается для дальнейшего использования
from main import vk, upload


def base_func(user_id, message, keyboard):
    """Общая функция, возвращает ответ на сообщение и клавиатуру"""
    vk.messages.send(user_id=user_id, message=message, random_id=get_random_id(),
                     keyboard=keyboard.get_keyboard())
    return True  # событие выполнено


def send_photo(user_id, url):
    """Функция отправки фото"""
    vk.messages.send(user_id=user_id, attachment=url,
                     random_id=get_random_id())
