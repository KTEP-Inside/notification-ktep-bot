import redis
from Bot.config_data.config import load_config


cfg = load_config()  # загружаем конфиг

# подключаемся к redis для хранения состояний
redis_client = redis.StrictRedis(host=cfg.db.db_host, port=6379, db=0, decode_responses=True)

# состояния
MENU = 'menu'
DOCUMENTS = 'documents'
PROFESSION = 'profession'
SCHEDULE = 'schedule'
COURSE_SCHEDULE = 'course_schedule'
ADMIN = 'admin'
ADD_ADMIN = 'add_admin'
START = 'start'
CHANGE_PHOTO = 'change_photo'
CHECK_PHOTO = 'check_photo'
