from Bot.handlers.admin_handlers import *
from Bot.lexicon.lexicon import LEXICON_admin_kb, LEXICON_photo_name
from Bot.services.services import get_state_and_photo
from Bot.state_machine.state_machine import *
from Bot.models.methods import check_admin


def admin_router(event, user_id):
    """Команды Админа"""
    request = 0
    admin = check_admin(user_id)  # проверка на админа
    text = event.message['text']  # получаем текст сообщения
    state = get_state_and_photo(user_id)  # получаем текущее состояние
    if admin:  # если пользователь админ
        # Проверки различных команд по их текстам и нужным состояниям
        if text == LEXICON_roles['admin']:
            request = handler_admin_role(user_id)
        elif text == LEXICON_admin_kb['add_admin'] \
                and state['state'] == ADMIN:
            request = handler_how_to_add_admin(user_id)
        elif state['state'] == ADD_ADMIN:
            # вызов ошибки или отработка по шаблонам
            if (re.search(r'https://vk\.com/[a-zA-Z0-9]{5,32}', event.message['text'])
                    or re.search('[a-zA-Z0-9]{5,32}', event.message['text'])):
                request = handler_add_admin(event, user_id)
            else:
                request = handler_add_admin_template_error(user_id)
        elif text == LEXICON_admin_kb['replace_photo'] and state['state'] == ADMIN:
            handler_check_photo(user_id)
        elif text in LEXICON_photo_name.values()\
                and state['state'] == CHECK_PHOTO:
            handler_write_photo(event, user_id)
        elif state['state'] == CHANGE_PHOTO:
            # Если есть медиа вложения
            if event.message['attachments']:
                # Если это фото
                if event.message['attachments'][0]['type'] == 'photo' \
                        and len(event.message['attachments']) == 1:
                    handler_replace_photo(event, user_id)
                else:
                    handler_error_replace_photo(user_id)
            else:
                handler_error_replace_photo(user_id)
        else:
            # неизвестная команда
            request = handler_not_admin_or_unknown(user_id)
    else:
        # не админ
        request = handler_not_admin_or_unknown(user_id)

    return request
