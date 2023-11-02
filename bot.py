import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from Bot.config_data import load_config

cfg = load_config()  # Загружаем конфиг

if not cfg.vk_bot.token:  # Проверка на наличие токена
    raise Exception('There is not token')

vk_session = vk_api.VkApi(token=cfg.vk_bot.token)  # Подключаемся к сессии vk_api
vk = vk_session.get_api()  # Подключаемся к интерфейсу api
upload = vk_api.VkUpload(vk)  # Создаём сеанс для загрузки фото

longpoll = VkBotLongPoll(vk_session, cfg.vk_bot.group_id, wait=25)  # Объект опроса сервера

if __name__ == '__main__':
    # Используем импорт здесь, чтобы избежать ошибки циклического импорта
    from Bot.routers import user_router
    from Bot.routers.admin_router import admin_router

    for event in longpoll.listen():  # Запускаем опрос

        if event.type == VkBotEventType.MESSAGE_NEW:  # Если сообщение новое

            user_id = event.message['from_id']  # ID пользователя
            if user_router(event, user_id):  # Опрашиваем user_router
                continue  # Ожидание событий
            if admin_router(event, user_id):  # Опрашиваем admin_router
                continue # Ожидание событий
