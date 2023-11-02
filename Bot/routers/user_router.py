import re

from Bot.handlers.base_handlers import handler_start
from Bot.lexicon.lexicon import LEXICON_roles, LEXICON_incoming_student
from Bot.handlers.user_handlers import *
from Bot.services.services import get_state_and_photo, register_user


def user_router(event, user_id):
    """Команды Студента или Абитуриента"""
    request = event.message['text']  # Получаем текст сообщения
    state = get_state_and_photo(user_id)  # Получаем текущее состояние

    if not state and request == LEXICON['start']:  # если у пользователя нет состояния и команда старт
        return handler_start(user_id)
    elif not state:
        return handler_start_error(user_id)

    if not event.obj['message']['attachments']:  # если в сообщении нет различного медиа-контента
        # Проверки различных команд по их текстам и нужным состояниям
        if request == LEXICON['menu']:
            return handler_menu(user_id)
        elif request == LEXICON['back']:
            return handler_back(user_id)
        elif request == LEXICON_roles['incoming_student'] and state['state'] == MENU:
            return handler_incoming_student(user_id)
        elif request == LEXICON_roles['student'] and state['state'] == MENU:
            return handler_student(user_id)
        elif request == LEXICON_incoming_student['admission_plan'] and state['state'] == DOCUMENTS:
            return handler_admission_plan(event, user_id)
        elif request == LEXICON_incoming_student['statement'] and state['state'] == DOCUMENTS:
            return handler_statement(user_id)
        elif request == LEXICON_incoming_student['documents'] and state['state'] == DOCUMENTS:
            return handler_documents(event, user_id)
        elif request == LEXICON_incoming_student['deadline'] and state['state'] == DOCUMENTS:
            return handler_deadline(user_id)
        elif request == LEXICON_incoming_student['questions'] and state['state'] == DOCUMENTS:
            return handler_questions(user_id)
        elif request == LEXICON_schedule['call_schedule'] and state['state'] == SCHEDULE:
            return handler_schedule_call(event, user_id)
        elif request == LEXICON_schedule['schedule'] and state['state'] == SCHEDULE:
            return handler_schedule(user_id)
        elif re.search(r'^\d{1}-й курс', request) and state['state'] == COURSE_SCHEDULE:
            return handler_schedule_course(event, user_id)
        elif re.search(r'^\d{2}.\d{2}.\d{2}$', request.split()[0][0:8]):
            return handler_profession(event, user_id)
