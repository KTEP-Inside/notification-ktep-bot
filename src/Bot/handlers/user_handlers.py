from Bot.handlers.base_handlers import handler_get_photo
from Bot.lexicon.lexicon import LEXICON, LEXICON_incoming_student_ans, LEXICON_prof_ans, LEXICON_schedule, \
    LEXICON_schedule_ans
from Bot.services.services import get_state_and_photo, set_state
from Bot.state_machine.state_machine import *
from Bot.commands.base_command import base_func
from Bot.handlers.admin_handlers import handler_admin_role, handler_check_photo
from Bot.keyboards.keyboards import schedule, courses_schedule, incoming_student, professions, roles, start_kb


# Handlers, связанные с разделом 'студент'
def handler_student(user_id):
    """Студент"""
    request = base_func(user_id, LEXICON['schedule'], schedule)  # клавиатура и ответ
    set_state(user_id, SCHEDULE)  # устанавливаем состояние пользователя
    return request


def handler_schedule_call(event, user_id):
    """Отправляем фото расписания звонков"""
    request = base_func(user_id, LEXICON_schedule_ans['call_schedule_ans'], schedule)  # клавиатура и ответ
    handler_get_photo(event, user_id)  # получаем фото для отправки и отправляем
    set_state(user_id, SCHEDULE)  # устанавливаем состояние пользователя
    return request


def handler_schedule(user_id):
    """Отправляем кнопки для выбора расписания по курсу"""
    request = base_func(user_id, LEXICON_schedule['schedule'], courses_schedule)  # клавиатура и ответ
    set_state(user_id, COURSE_SCHEDULE)  # устанавливаем состояние пользователя
    return request


def handler_schedule_course(event, user_id):
    """Отправляем расписание выбранного курса"""
    request = base_func(user_id, LEXICON_schedule_ans[event.message['text'][0] + '_course_ans'],
                        courses_schedule)  # клавиатура и ответ
    handler_get_photo(event, user_id)  # получаем фото для отправки и отправляем
    set_state(user_id, COURSE_SCHEDULE)  # устанавливаем состояние пользователя
    return request


# Handlers, связанные с разделом 'абитуриент'
def handler_incoming_student(user_id):
    """Абитуриент"""
    request = base_func(user_id, LEXICON['statement'], incoming_student)  # клавиатура и ответ
    set_state(user_id, DOCUMENTS)  # устанавливаем состояние пользователя
    return request


# Раздел с информацией для поступления
def handler_admission_plan(event, user_id):
    """Отправляем фото плана поступления и специальности"""
    request = base_func(user_id, LEXICON_incoming_student_ans['admission_plan_ans'],
                        professions)  # клавиатура и ответ
    handler_get_photo(event, user_id)  # получаем фото для отправки и отправляем
    set_state(user_id, PROFESSION)  # устанавливаем состояние пользователя
    return request


# Обработка различных специальностей
def handler_profession(event, user_id):
    """Отправляем информацию о выбранной специальности"""
    request = base_func(user_id, LEXICON_prof_ans[event.message['text'].split()[0]],
                        professions)  # клавиатура и ответ
    set_state(user_id, PROFESSION)  # устанавливаем состояние пользователя
    return request


def handler_statement(user_id):
    """Информация для подачи документов"""
    request = base_func(user_id, LEXICON_incoming_student_ans['statement_ans'],
                        incoming_student)  # клавиатура и ответ
    set_state(user_id, DOCUMENTS)  # устанавливаем состояние пользователя
    return request


def handler_documents(event, user_id):
    """Необходимые документы"""
    request = base_func(user_id, LEXICON_incoming_student_ans['documents_ans'],
                        incoming_student)  # клавиатура и ответ
    handler_get_photo(event, user_id)  # получаем фото для отправки и отправляем
    set_state(user_id, DOCUMENTS)  # устанавливаем состояние пользователя
    return request


def handler_deadline(user_id):
    """Сроки подачи документов"""
    request = base_func(user_id, LEXICON_incoming_student_ans['deadline_ans'],
                        incoming_student)  # клавиатура и ответ
    set_state(user_id, DOCUMENTS)  # устанавливаем состояние пользователя
    return request


def handler_questions(user_id):
    """Если остались вопросы"""
    request = base_func(user_id, LEXICON_incoming_student_ans['questions_ans'],
                        incoming_student)  # клавиатура и ответ
    set_state(user_id, DOCUMENTS)  # устанавливаем состояние пользователя
    return request


def handler_menu(user_id):
    """Используется для вывода меню из любой точки бота"""
    request = base_func(user_id, LEXICON['your_role'], roles)  # клавиатура и ответ
    set_state(user_id, MENU)  # устанавливаем состояние пользователя
    return request


def handler_start_error(user_id):
    """Пользователь не нажал кнопку начать в начале"""
    request = base_func(user_id, LEXICON['error_start'], start_kb)   # клавиатура и ответ
    return request


def handler_back(user_id):
    """Обработка нажатия кнопки назад из различных частей бота"""
    request = 0

    user = get_state_and_photo(user_id)  # получаем состояние пользователя
    if user['state'] == SCHEDULE:
        request = handler_menu(user_id)
    elif user['state'] == ADMIN:
        request = handler_menu(user_id)
    elif user['state'] == DOCUMENTS:
        request = handler_menu(user_id)
    elif user['state'] == COURSE_SCHEDULE:
        request = handler_student(user_id)
    elif user['state'] == PROFESSION:
        request = handler_incoming_student(user_id)
    elif user['state'] == ADD_ADMIN:
        request = handler_admin_role(user_id)
    elif user['state'] == CHANGE_PHOTO:
        request = handler_check_photo(user_id)
    elif user['state'] == CHECK_PHOTO:
        request = handler_admin_role(user_id)

    return request
