from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from Bot.lexicon.lexicon import *


def add_base_buttons(keyboard: VkKeyboard):
    """Добавляем кнопки назад, меню и ссылку через единый интерфейс"""

    keyboard.add_button(label=LEXICON['back'], color=VkKeyboardColor.NEGATIVE)
    keyboard.add_button(label=LEXICON['menu'], color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_openlink_button(label=LEXICON['ktep'], link=LEXICON['ktep_link'])


base_kb = VkKeyboard(one_time=False)  # Клавиатура с базовыми кнопками
add_base_buttons(base_kb)

# клавиатура выбора специальности
professions = VkKeyboard(one_time=False)
counter = 0
for i in LEXICON_prof.keys():
    professions.add_button(label=LEXICON_prof[i], color=VkKeyboardColor.POSITIVE)
    # используем данную конструкцию для нужно отображения кнопок(из-за лимитов vk_api)
    if counter % 2 == 0:
        professions.add_line()
    counter += 1
add_base_buttons(professions)


# клавиатура с информацией для абитуриента
incoming_student = VkKeyboard(one_time=False)
for i in LEXICON_incoming_student:
    incoming_student.add_button(label=LEXICON_incoming_student[i], color=VkKeyboardColor.POSITIVE)
    incoming_student.add_line()
add_base_buttons(incoming_student)


# клавиатура ролей
roles = VkKeyboard(one_time=False)
for role in LEXICON_roles.keys():
    roles.add_button(label=LEXICON_roles[role], color=VkKeyboardColor.POSITIVE)
    roles.add_line()
roles.add_openlink_button(label=LEXICON['ktep'], link=LEXICON['ktep_link'])


# клавиатура для выбора расписание звонков / обычное расписание
schedule = VkKeyboard(one_time=False)
for i in LEXICON_schedule.keys():
    schedule.add_button(label=LEXICON_schedule[i], color=VkKeyboardColor.POSITIVE)
    schedule.add_line()
add_base_buttons(schedule)


# клавиатура для выбора расписания по курсу
courses_schedule = VkKeyboard(one_time=False)
for i in LEXICON_courses.keys():
    courses_schedule.add_button(label=LEXICON_courses[i], color=VkKeyboardColor.POSITIVE)
    courses_schedule.add_line()
add_base_buttons(courses_schedule)


# кнопка старт и ссылка
start_kb = VkKeyboard(one_time=False)
start_kb.add_button(label=LEXICON['start'], color=VkKeyboardColor.PRIMARY)
start_kb.add_line()
start_kb.add_openlink_button(label=LEXICON['ktep'], link=LEXICON['ktep_link'])

# клавиатура с меню администратора
admin_menu_kb = VkKeyboard(one_time=False)
for button in LEXICON_admin_kb.keys():
    admin_menu_kb.add_button(label=LEXICON_admin_kb[button], color=VkKeyboardColor.POSITIVE)
    admin_menu_kb.add_line()
add_base_buttons(admin_menu_kb)


# клавиатура с выбором фото для изменения
counter = 0
change_photo_kb = VkKeyboard(one_time=False)
for button in LEXICON_photo_name.keys():
    change_photo_kb.add_button(label=LEXICON_photo_name[button], color=VkKeyboardColor.POSITIVE)
    if counter % 2 != 0:
        change_photo_kb.add_line()
    counter += 1
add_base_buttons(change_photo_kb)

