import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import psycopg2
from dotenv import load_dotenv
from os import environ, environb

load_dotenv()

print(environ.values(), environb.values())

TOKEN = environ['TOKEN']
DB_USER = environ['DB_USER']
DB_PASSWORD = environ['DB_PASSWORD']
DB_NAME = environ['DB_NAME']
DB_HOST = environ['DB_HOST']
DB_PORT = environ['DB_PORT']

if TOKEN == None:
    raise Exception('There is not token')
authorize = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(authorize)
connection = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
# объект, который позволяет выполнять любые операции записи/чтения в базе
cursor = connection.cursor()

menu = VkKeyboard(one_time=False)
menu.add_button('План поступления', color=VkKeyboardColor.POSITIVE)
menu.add_line()
menu.add_button('Как представить заявление \U00002709',
                color=VkKeyboardColor.POSITIVE)
menu.add_line()
menu.add_button('Документы, необходимые для поступления \U0001F4EA',
                color=VkKeyboardColor.POSITIVE)
menu.add_line()
menu.add_button('Сроки подачи документов \U0001F4EB',
                color=VkKeyboardColor.POSITIVE)
menu.add_line()
menu.add_button('Если остались вопросы \U0000260E',
                color=VkKeyboardColor.POSITIVE)
menu.add_line()
menu.add_button('Меню \U000021A9', color=VkKeyboardColor.NEGATIVE)

prof = VkKeyboard(one_time=False)
prof.add_button('09.02.01', color=VkKeyboardColor.POSITIVE)
prof.add_line()
prof.add_button('09.02.06', color=VkKeyboardColor.POSITIVE)
prof.add_line()
prof.add_button('09.02.07 Программиcт', color=VkKeyboardColor.POSITIVE)
prof.add_line()
prof.add_button('09.02.07 Тестировщик', color=VkKeyboardColor.POSITIVE)
prof.add_line()
prof.add_button('10.02.04', color=VkKeyboardColor.POSITIVE)
prof.add_line()
prof.add_button('11.02.13', color=VkKeyboardColor.POSITIVE)
prof.add_line()
prof.add_button('11.02.16', color=VkKeyboardColor.POSITIVE)
prof.add_line()
prof.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

keyboard = VkKeyboard(one_time=False)
keyboard.add_button('Меню вопросов', color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_openlink_button('Официальный сайт КТЭП',
                             link='https://ktep40.ru/')

abiturient = VkKeyboard(one_time=False)
abiturient.add_button('Студент', color=VkKeyboardColor.POSITIVE)
abiturient.add_line()
abiturient.add_button('Абитуриент', color=VkKeyboardColor.POSITIVE)
abiturient.add_line()
abiturient.add_button('Админ', color=VkKeyboardColor.POSITIVE)

starts = VkKeyboard(one_time=False)
starts.add_button('Начать', color=VkKeyboardColor.POSITIVE)
starts.add_line()
starts.add_openlink_button('Официальный сайт КТЭП',
                           link='https://ktep40.ru/')

ksk = VkKeyboard(one_time=False)
ksk.add_button('КСК', color=VkKeyboardColor.POSITIVE)
ksk.add_line()
ksk.add_button('ИСиП(п)', color=VkKeyboardColor.POSITIVE)
ksk.add_line()
ksk.add_button('СиСадм', color=VkKeyboardColor.POSITIVE)
ksk.add_line()
ksk.add_button('Рп', color=VkKeyboardColor.POSITIVE)
ksk.add_line()
ksk.add_button('Тэ', color=VkKeyboardColor.POSITIVE)
ksk.add_line()
ksk.add_button('Мтор Эпу', color=VkKeyboardColor.POSITIVE)
ksk.add_line()
ksk.add_button('ИСиП(т)', color=VkKeyboardColor.POSITIVE)

rass = VkKeyboard(one_time=False)
rass.add_button('Рассылка для студентов', color=VkKeyboardColor.POSITIVE)
rass.add_line()
rass.add_button('Рассылка для абитуриентов', color=VkKeyboardColor.POSITIVE)

number = VkKeyboard(one_time=False)
number.add_button('1', color=VkKeyboardColor.POSITIVE)
number.add_line()
number.add_button('2', color=VkKeyboardColor.POSITIVE)
number.add_line()
number.add_button('3', color=VkKeyboardColor.POSITIVE)
number.add_line()
number.add_button('4', color=VkKeyboardColor.POSITIVE)
number.add_line()
number.add_button('5', color=VkKeyboardColor.POSITIVE)

numberaspisanie = VkKeyboard(one_time=False)
numberaspisanie.add_button('Для первых курсов', color=VkKeyboardColor.POSITIVE)
numberaspisanie.add_line()
numberaspisanie.add_button('Для вторых курсов', color=VkKeyboardColor.POSITIVE)
numberaspisanie.add_line()
numberaspisanie.add_button(
    'Для третьих курсов', color=VkKeyboardColor.POSITIVE)
numberaspisanie.add_line()
numberaspisanie.add_button('Для четвертых курсов',
                           color=VkKeyboardColor.POSITIVE)
numberaspisanie.add_line()
numberaspisanie.add_button('Для пятых курсов', color=VkKeyboardColor.POSITIVE)
numberaspisanie.add_line()
numberaspisanie.add_button('Вернуться', color=VkKeyboardColor.NEGATIVE)

raspisanie = VkKeyboard(one_time=False)
raspisanie.add_button('Расписание', color=VkKeyboardColor.POSITIVE)
raspisanie.add_line()
raspisanie.add_button('Расписание звонков', color=VkKeyboardColor.POSITIVE)
raspisanie.add_line()
raspisanie.add_button('Меню', color=VkKeyboardColor.NEGATIVE)


# создаем функции

def numberrass(sender, message):
    authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                       'keyboard': numberaspisanie.get_keyboard()})


def start(sender, message):
    authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                       'keyboard': starts.get_keyboard()})


def write_role(sender, message):
    authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                       'keyboard': abiturient.get_keyboard()})


def write(sender, message):
    authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                       'keyboard': abiturient.get_keyboard()})


def raspisanie1(sender, message):
    authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                       'keyboard': raspisanie.get_keyboard()})


def rassilka(sender, message):
    authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                       'keyboard': rass.get_keyboard()})


def write_prof(sender, message):
    authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                       'keyboard': prof.get_keyboard()})


def write_message2(sender, message):
    authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                       'keyboard': menu.get_keyboard()})


def kurs(sender, message):
    authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                       'keyboard': ksk.get_keyboard()})


def write_number(sender, message):
    authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                       'keyboard': number.get_keyboard()})


def send_photo(sender, url):
    authorize.method('messages.send', {
                     'user_id': sender, 'attachment': url, "random_id": get_random_id()})


def send_stick(sender, number):
    authorize.method('messages.send', {
                     'user_id': sender, 'sticker_id': number, "random_id": get_random_id()})


def insert_abiturient(user_id):
    with connection.cursor() as cursor:
        # Проверяем, существует ли пользователь уже в базе данных
        cursor.execute(
            "SELECT id_users FROM users WHERE id_users = %s", (user_id,))
        existing_user = cursor.fetchone()

        if existing_user:
            # Пользователь уже существует в системе
            write_message2(msg, 'Что вас интересует?')
        else:
            # Получаем id_role для роли "абитуриент" из таблицы "role"
            cursor.execute(
                "SELECT id_role FROM role WHERE role = 'АБИТУРИЕНТ'")
            id_role = cursor.fetchone()[0]

            # Вставляем данные пользователя в таблицу "users"
            cursor.execute(
                "INSERT INTO users (id_users, id_role, id_kurs, admin, number_kurs) VALUES (%s, %s, %s, %s, %s)",
                (user_id, id_role, None, False, None))

            connection.commit()
            write_message2(msg, 'Что вас интересует')


def insert_student(user_id):
    with connection.cursor() as cursor:
        # Проверяем, существует ли пользователь уже в базе данных
        cursor.execute(
            "SELECT id_users FROM users WHERE id_users = %s", (user_id,))
        existing_user = cursor.fetchone()

        if existing_user:
            # Пользователь уже существует в системе
            raspisanie1(msg, 'Ваше расписание')
        else:
            # Получаем id_role для роли "студент" из таблицы role
            cursor.execute("SELECT id_role FROM role WHERE role = 'СТУДЕНТ'")
            id_role = cursor.fetchone()[0]

            # Вставляем данные пользователя в таблицу users
            cursor.execute(
                "INSERT INTO users (id_users, id_role, id_kurs, admin, number_kurs) VALUES (%s, %s, %s, %s, %s)",
                (user_id, id_role, None, False, None))

            connection.commit()
            kurs(msg, 'Ваша группа')


# предназначена для обработки нажатия кнопки пользователем. Она принимает два аргумента: user_id - идентификатор пользователя, и button_text - текст кнопки, которую пользователь нажал.
def handle_button_click(user_id, button_text):
    with connection.cursor() as cursor:
        # Получение id_role для роли "студент" из таблицы "role"
        cursor.execute("SELECT id_role FROM role WHERE role = 'СТУДЕНТ'")
        id_role = cursor.fetchone()[0]

        # Получение id_kurs для курса на основе текста кнопки
        cursor.execute(
            "SELECT id_kurs FROM kurs WHERE kurs = %s", (button_text,))
        id_kurs = cursor.fetchone()[0]

        # Проверка, существует ли пользователь уже в таблице "users"
        cursor.execute(
            "SELECT id_users FROM users WHERE id_users = %s", (user_id,))
        existing_user = cursor.fetchone()

        if existing_user:
            # Обновление данных существующего пользователя
            cursor.execute(
                "UPDATE users SET id_role = %s, id_kurs = %s, admin = FALSE, number_kurs = NULL WHERE id_users = %s",
                (id_role, id_kurs, user_id))
        else:
            # Вставка новых данных пользователя в таблицу "users"
            cursor.execute(
                "INSERT INTO users (id_users, id_role, id_kurs, admin, number_kurs) VALUES (%s, %s, %s, FALSE, NULL)",
                (user_id, id_role, id_kurs))

    connection.commit()


def update_number_kurs(number_kurs):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE users SET number_kurs = %s",
            number_kurs)
    connection.commit()


def create_tables():
    SQL = [
        'CREATE TABLE IF NOT EXISTS role(\
            id_role SERIAL PRIMARY KEY,\
            role VARCHAR(20) UNIQUE\
            );', 'CREATE TABLE IF NOT EXISTS kurs(\
            id_kurs SERIAL PRIMARY KEY,\
            kurs VARCHAR(30) UNIQUE\
            );', 'CREATE TABLE IF NOT EXISTS users(\
            id_users INT PRIMARY KEY,\
            id_role INT,\
            id_kurs INT,\
            admin BOOLEAN DEFAULT false,\
            number_kurs SMALLINT,\
            FOREIGN KEY (id_role) references role(id_role),\
            FOREIGN KEY (id_kurs) references kurs(id_kurs)\
            );'
    ]
    for sql in SQL:
        with connection.cursor() as cursor:
            cursor.execute(sql)
        connection.commit()


def insert_roles():
    roles = ['СТУДЕНТ', "АБИТУРИЕНТ"]
    for role in roles:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM role WHERE role = %s", (role,))
            exists = cursor.fetchone()
            if not exists:
                cursor.execute(
                    "INSERT INTO role(role) VALUES(%s)", (role,))
                connection.commit()


def insert_kurs():
    kurses = ['КСК', "ИСиП(п)", "СиСадм", "Рп", "Тэ", "Мтор Эпу", "ИСиП(т)"]
    for kurs in kurses:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM kurs WHERE kurs = %s", (kurs,))
            exists = cursor.fetchone()
            if not exists:
                cursor.execute(
                    "INSERT INTO kurs(kurs) VALUES(%s)", (kurs,))
                connection.commit()


create_tables()
insert_roles()
insert_kurs()


# Флаг, указывающий, отправляет ли администратор сообщение студентам
is_admin_sending = False
# Флаг, указывающий, отправляет ли администратор сообщение абитуриетам
is_admin_send = False
admin_message = None  # Переменная для хранения сообщения администратора

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        message = event.text.lower()
        msg = event.user_id

        match message:
            case 'начать':
                write_role(msg, 'Ваша роль')
            case 'пока':
                start(msg, 'Пока')
                send_stick(msg, 15791)
            case 'привет':
                start(msg, 'Привет' + u"\U0001F60A")
                send_stick(msg, 3)
            case "студент":
                insert_student(msg)

            case 'админ':
                rassilka(msg, 'Кому отправить?')
            case 'расписание':
                numberrass(msg, 'Выбирайте курс')
            case 'расписание звонков':
                send_photo(msg,
                           'https://sun9-13.userapi.com/impg/b97vMBIZTS8iFEldYNZbkWgC2AuF0YMMoHLsPg/RC2wiDhwi34.jpg?size=404x538&quality=96&sign=7c8d47721088b6d26c82f50ce8b225b5&type=album')
            case 'для первых курсов':
                send_photo(msg,
                           'https://sun9-79.userapi.com/impg/DjyHVxKiCLzsVFOxjIJJUWuzYaTAmV8MjiXtoQ/lB3i9GMMBRU.jpg?size=1146x755&quality=96&sign=152508d74f2da301d19bf7e7be6ecb23&type=album')
            case 'для третьих курсов':
                send_photo(msg,
                           'https://sun9-33.userapi.com/impg/DWfVJHMkELYAh_SA7xUKI0PbdNIiafSbdU3cUQ/laBpsddT4QE.jpg?size=2560x1810&quality=96&sign=c0501a5b9add8049d0beadc15800b3b1&type=album')
            case 'для четвертых курсов':
                send_photo(msg,
                           'https://sun1-15.userapi.com/impg/xwUrWajvxrr2Bz3kUZAdcctMFDizKwdHAIeuRA/u3sbKUKdeco.jpg?size=2560x1810&quality=96&sign=a1f602fe0944cb3cf4794111234fd6a3&type=album')
            case 'для пятых курсов':
                send_photo(msg,
                           'https://sun9-54.userapi.com/impg/QiOCX9RPddnVkbWmIXUjQmlibHfP91jCG5LHXw/fOOW6MJBWFI.jpg?size=1669x2160&quality=96&sign=8791e3e8db7cb3134d2db07bec424137&type=album')
            case 'для вторых курсов':
                send_photo(msg,
                           'https://sun1-24.userapi.com/impg/KOunJ6jNwAYcFx9eZL5F2EEONIzYiVsRthAl6A/UnSmE2V4ex4.jpg?size=2481x1754&quality=96&sign=02c6c51cc12a54e3e35972b53bcc2d58&type=album')
            case 'вернуться':
                raspisanie1(msg, 'Выберите действие')
            case 'кск':
                handle_button_click(msg, 'КСК')
                write_number(msg, 'Ваш номер курса?')

            case 'исип(п)':
                handle_button_click(msg, 'ИСиП(п)')
                write_number(msg, 'Ваш номер курса?')

            case 'сисадм':
                handle_button_click(msg, 'СиСадм')
                write_number(msg, 'Ваш номер курса?')

            case 'рп':
                handle_button_click(msg, 'Рп')
                write_number(msg, 'Ваш номер курса?')

            case 'тэ':
                handle_button_click(msg, 'Тэ')
                write_number(msg, 'Ваш номер курса?')
            case 'исип(т)':
                handle_button_click(msg, 'ИСиП(т)')
                write_number(msg, 'Ваш номер курса?')

            case 'мтор эпу':
                handle_button_click(msg, 'Мтор Эпу')
                write_number(msg, 'Ваш номер курса?')

            case '1':
                update_number_kurs('1')
                write_role(msg, 'Вы в базе')

            case '2':
                update_number_kurs('2')
                write_role(msg, 'Вы в базе')

            case '3':
                update_number_kurs('3')
                write_role(msg, 'Вы в базе')

            case '4':
                update_number_kurs('4')
                write_role(msg, 'Вы в базе')

            case '5':
                update_number_kurs('5')
                write_role(msg, 'Вы в базе')

            case "абитуриент":
                insert_abiturient(msg)

            case 'план поступления':
                write_prof(msg, 'Что вас интересует?')
                send_photo(msg,
                           'https://sun1-21.userapi.com/impg/WLCQLm0Egh21kUyjYZgWOc3XE575qC5tDAKk4w/3OeQxGN8GXI.jpg?size=1080x656&quality=96&sign=2cf674694ae8c51fc3cf426f8c0242a3&type=album')
            case '09.02.01':
                write_prof(msg,
                           'По специальности 09.02.01 Компьютерные системы и комплексы техникум готовит техника по компьютерным системам, который проектирует, конструирует, настраивает, обслуживает компьютерные сети, средства вычислительной техники, мониторы, принтеры, сканеры и др.\n\nПредприятия: АО "Тайфун", АО "Калуга Астрал", КФ ПАО "Ростелеком", ПАО "Сбербанк".\n\nСпециалист в этой области знает устройство плат, микропроцессоров\n\nИсточник: https://ktep40.ru/spetsialnosti/09-02-01-kompyuternye-sistemy-i-kompleksy/')

            case '09.02.06':
                write_prof(msg,
                           'По специальности 09.02.06 Сетевое и системное администрирование техникум готовит техника, который выполняет работы по проектированию сетевой инфраструктуры, сетевому администрированию, эксплуатации объектов сетевой инфраструктуры.\n\nСетевой и системный администратор (он же IT-администратор, сисадмин) – это специалист, который обеспечивает штатную работу парка компьютерной техники в компании или организации, правильную работу компьютерной сети и имеющегося программного обеспечения, а также отвечает за информационную безопасность организации.\n\nПредприятия: АО "Тайфун", АО "Калуга Астрал", КФ ПАО "Ростелеком", ПАО "Сбербанк"\n\nИсточник:https://ktep40.ru/spetsialnosti/09-02-06-setevoe-i-sistemnoe-administrirovanie/')
            case '09.02.07 программиcт':
                write_prof(msg,
                           'По специальности 09.02.07 Информационные системы и программирование техникум готовит программистов, который принимает участие в разработке, отладке, проверке работоспособности, модификации программного обеспечения.\n\nПредприятия: АО "Тайфун", АО "Калуга Астрал", КФ ПАО "Ростелеком", ООО "Каскад инжиниринг", ООО "АйТи-комплекс", ПАО "Сбербанк"\n\nСпециалист может выполнять следующие виды деятельности:\n- разработка модулей программного обеспечения для компьютерных систем;\n- осуществление интеграции программных модулей;\n- сопровождение и обслуживание программного обеспечения компьютерных систем;\n- разработка, администрирование и защита баз данных.\n\nИсточник:https://ktep40.ru/spetsialnosti/09-02-07-informatsionnye-sistemy-i-programmirovanie-programmist/')
            case '09.02.07 тестировщик':
                write_prof(msg,
                           'По специальности 09.02.07 Информационные системы и программирование техникум готовит специалистов по тестированию в области информационных технологий\n\nПредприятия: АО "Тайфун", АО "Калуга Астрал", КФ ПАО "Ростелеком", ООО "Каскад инжиниринг", ООО "АйТи-комплекс", ПАО "Сбербанк"\n\nСпециалист может выполнять следующие виды деятельности:\n- разработка модулей программного обеспечения для компьютерных систем;\n- осуществление интеграции программных модулей;\n- сопровождение и обслуживание программного обеспечения компьютерных систем;\n- разработка, администрирование и защита баз данных.\n\nИсточник:https://ktep40.ru/spetsialnosti/09-02-07-informatsionnye-sistemy-i-programmirovanie-spetsialist-po-testirovaniyu-v-oblasti-informats/')
            case '10.02.04':
                write_prof(msg,
                           'Специальность - 10.02.04 Обеспечение информационной безопасности телекоммуникационных систем.\n\nОбласть профессиональной деятельности выпускников:\n-обеспечение безопасности информации в компьютерных системах и сетях в условиях существования угроз их информационной безопасности;\n-обеспечение защиты средств связи сетей электросвязи (СССЭ) от несанкционированного доступа к ним (НСД) в условиях существования угроз их информационной безопасности (ИБ);\n-повышение эффективности поддержки процессов принятия решений в государственных органах, обеспечивающих национальную безопасность, за счет создания и применения информационно-аналитических систем в защищенном исполнении (ИАС);\n-обеспечение безопасности информации в автоматизированных системах, функционирующих в условиях существования угроз в информационной сфере и обладающих информационно- технологическими ресурсами, подлежащими защите;\n-предотвращение утечки информации ограниченного доступа по техническим каналам в результате несанкционированного доступа к информации и специальных воздействий на информацию (носители информации) в целях ее добывания, уничтожения, искажения и блокирования доступа к ней.\n\nКвалификация: техник по защите информацииn\n\nИсточник:https://ktep40.ru/spetsialnosti/10-02-04-obespechenie-informatsionnoy-bezopasnosti-telekommunikatsionnykh-sistem/')
            case '11.02.13':
                write_prof(msg,
                           'По специальности 11.02.13 Твердотельная электроника техникум готовит техника, который участвует в разработке технологических процессов, в монтаже, регулировке, техническом обслуживании и эксплуатации технологического оборудования для изготовления изделий твердотельной электроники.\n\nПредприятия: АО "Восход" - КРЛЗ, АО "ОКБ МЭЛ", ООО "СмартТермоэлектрикс", АО "Информтехника и Связь", ООО "Фокон".\n\nВыпускники участвуют в изготовлении микросхем различного типа для военной, космической, бытовой техники, компьютеров. Наши выпускники получают знания по основам проектирования интегральных микросхем, подробно изучают современное оборудование для изготовления этих микросхем.\n\nИсточник:https://ktep40.ru/spetsialnosti/11-02-13-tverdotelnaya-elektronika/')
            case '11.02.16':
                write_prof(msg,
                           'По специальности 11.02.16 Монтаж, техническое обслуживание и ремонт электронных приборов и устройств техникум готовит техника, который участвует в конструировании и проектировании электронных приборов и устройств, в разработке базовых элементов для оснащения промышленных и бытовых вычислительных систем.\n\nПредприятия: АО "Тайфун", АО "Информтехника и Связь", АО "КЗТА", АО "Восход"-КРЛЗ, ООО "НПО "Телеметрия", ООО "Фокон", АО "КЭМЗ", АО "НПФ "Сигма", АО "Автоэлектроника", АО "Калугаприбор"\n\nСоздание чертежей и технологий (техник-конструктор, техник-технолог), сборка, монтаж, регулировка изделий (слесарь-сборщик, электромонтажник, регулировщик), управляет производственным процессом (мастер производственного участка), обслуживает оборудование и осуществляет контроль качества изделий (контролер, наладчик технологического оборудования).\n\nИсточник:https://ktep40.ru/spetsialnosti/11-02-16-montazh-tekhnicheskoe-obsluzhivanie-i-remont-elektronnykh-priborov-i-ustroystv/')
            case 'назад':
                write_message2(msg, 'Меню')
            case 'меню \U000021A9':
                start(msg, 'Главное меню')
            case 'меню':
                start(msg, 'Главное меню')
            case 'как представить заявление \U00002709':
                write_message2(msg,
                               'Лично в Техникуме\n \U00002709 Через операторов почтовой связи заказным письмом с уведомлением о вручении\n \U0001F4EE Посредством электронной почты uchast.ktep@gmail.com\n \U0001F4F1С помощью использования функционала «Единый портал государственных и муниципальных услуг')
            case 'документы, необходимые для поступления \U0001F4EA':
                write_message2(msg,
                               'Вам нужно:\n1) Заявление поступающего\n2) Оригинал или ксерокопию паспорта поступающего\n3) СНИЛС поступающего\n4) Оригинал или ксерокопия аттестата об основном общем образовании\n5) Фотографии размером 3х4 (4штуки)\n6) Медицинская справка формы 086-у\n7) Согласие родителей на обработку персональных данных ребенка\n8) Согласие родителей на видеонаблюдение\n9) Согласие родителей на обработку персональных данных ребенка третьими лицами (централизованная бухгалтерия\n\nА так-же')
                send_photo(msg,
                           'https://sun9-34.userapi.com/impg/w0otbT4TKY4OZjSTqhz-ehBpKcXYNQgp6lGFNQ/dVK1obFq71E.jpg?size=997x225&quality=96&sign=3b1cf3ecc3f04357b83dc248eb9b43c7&type=album')
            case 'сроки подачи документов \U0001F4EB':
                write_message2(msg,
                               '\U000026A0Прием документов на первый курс очного отделения осуществляется с 19 июня до 15 августа 2023 года, а при наличии свободных мест прием документов продлевается до 25 ноября 2023 года\U000026A0')
            case 'если остались вопросы \U0000260E':
                write_message2(msg, 'Позвоните 8(4842)73-71-01')
            case "рассылка для студентов":
                admin_id = msg  # Получаем ID пользователя администратора

                # Проверяем, является ли пользователь администратором
                cursor.execute("SELECT * FROM users WHERE id_users = CAST(%s AS integer) AND admin = 'true'",
                               (admin_id,))
                admin = cursor.fetchone()

                if admin:
                    # Пользователь является администратором
                    rassilka(msg, 'Вы являетесь администратором')
                    # Устанавливаем флаг, указывающий, что администратор отправляет сообщение
                    is_admin_sending = True

                else:
                    # Пользователь не является администратором
                    start(msg, 'Вы не являетесь администратором')
                    # Сбрасываем флаг, чтобы избежать непрерывной отправки сообщений
                    is_admin_sending = False

            case 'рассылка для абитуриентов':
                admin_id = msg  # Получаем ID пользователя администратора

                # Проверяем, является ли пользователь администратором
                cursor.execute("SELECT * FROM users WHERE id_users = CAST(%s AS integer) AND admin = 'true'",
                               (admin_id,))
                admin = cursor.fetchone()

                if admin:
                    # Пользователь является администратором
                    rassilka(msg, 'Вы являетесь администратором')
                    # Устанавливаем флаг, указывающий, что администратор отправляет сообщение
                    is_admin_send = True

                else:
                    # Пользователь не является администратором
                    start(msg, 'Вы не являетесь администратором')
                    is_admin_send = False  # Сбрасываем флаг, чтобы избежать непрерывной отправки сообщений
            case _:
                if is_admin_sending:
                    if message:  # есть ли в сообщении текст (message)
                        admin_message = message  # значение переменной admin_message обновляется этим текстом
                    else:
                        write_role(msg, 'Неизвестная команда')
                elif is_admin_send:
                    if message:
                        admin_message = message
                    else:
                        write_role(msg, 'Неизвестная команда')

                # Проверяем, задано ли сообщение администратора и флаг установлен в True
                # проверяем, установлены ли флаг is_admin_send и задано ли сообщение администратора (admin_message).
                if is_admin_send and admin_message:
                    # Получаем список студентов
                    # выполняем запрос к базе данных, чтобы получить список студентов с ролью "абитуриент" (id_role = '1').
                    cursor.execute(
                        "SELECT id_users FROM users WHERE id_role = '1'")
                    students = cursor.fetchall()

                    if students:
                        # Отправляем сообщение студентам
                        for student in students:
                            student_id = student[0]
                            write(student_id, admin_message)
                    else:
                        write_role(msg, 'Нет абитуриентав для рассылки.')

                    # Сбрасываем флаг и сообщение администратора после завершения отправки сообщения
                    is_admin_send = False
                    admin_message = None

                elif is_admin_sending and admin_message:
                    # Получаем список абитуриентов
                    cursor.execute(
                        "SELECT id_users FROM users WHERE id_role = '2'")
                    applicants = cursor.fetchall()

                    if applicants:
                        # Отправляем сообщение абитуриентам
                        for applicant in applicants:
                            applicant_id = applicant[0]
                            write(applicant_id, admin_message)
                    else:
                        write_role(msg, 'Нет студетов для рассылки.')

                    # Сбрасываем флаг и сообщение администратора после завершения отправки сообщения
                    is_admin_sending = False
                    admin_message = None
                else:
                    write_role(msg, 'Команда неизвестна')
