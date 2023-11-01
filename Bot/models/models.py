from peewee import Model, CharField, MySQLDatabase, IntegerField
from Bot.config_data.config import load_config

cfg = load_config()  # загружаем конфиг

db = MySQLDatabase(database=cfg.db.db_name, user=cfg.db.db_user, password=cfg.db.db_password,
                   host=cfg.db.db_host)  # подключаемся к бд


class BaseDataBase(Model):
    """Базовая модель"""
    class Meta:
        database = db


class ImageModel(BaseDataBase):
    """Модель для хранения пути и названия фото"""
    image_name = CharField(max_length=50, unique=True, primary_key=True)
    image_path = CharField(max_length=250)

    class Meta:
        table_name = 'image'


class AdminModel(BaseDataBase):
    """Модель для хранения id админов"""
    admin_id = IntegerField(unique=True, primary_key=True)

    class Meta:
        table_name = 'admin'


db.connect()

db.create_tables([ImageModel, AdminModel])  # создаем таблицы

db.close()