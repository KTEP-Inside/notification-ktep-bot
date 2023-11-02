from dataclasses import dataclass
from environs import Env


@dataclass
class VkBot:
    token: str
    group_id: int


@dataclass
class DataBaseConfig:
    db_name: str
    db_user: str
    db_host: str
    db_password: str
    db_port: int


@dataclass
class StateStorage:
    host: str
    port: int
    list: int | None = 0


@dataclass
class Config:
    vk_bot: VkBot
    db: DataBaseConfig
    state_storage: StateStorage


def load_config(path: str = None) -> Config:
    """Считываем файл .env и получаем нужные переменные"""
    env: Env = Env()
    env.read_env(path)

    cfg = Config(
        vk_bot=VkBot(
            token=env('BOT_TOKEN'),
            group_id=int(env('GROUP_ID'))
        ),
        db=DataBaseConfig(
            db_name=env('DB_NAME'),
            db_host=env('DB_HOST'),
            db_user=env('DB_USER'),
            db_password=env('DB_PASSWORD'),
            db_port=int(env('DB_PORT'))
        ),
        state_storage=StateStorage(
            host=env('STATE_STORAGE_HOST'),
            port=int(env('STATE_STORAGE_PORT')),
            list=int(env('STATE_STORAGE_LIST'))
        )
    )
    return cfg
