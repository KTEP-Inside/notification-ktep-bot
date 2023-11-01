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


@dataclass
class Config:
    vk_bot: VkBot
    db: DataBaseConfig


def load_config(path: str = None) -> Config:
    """Считываем файл .env и получаем нужные переменные"""
    env: Env = Env()
    env.read_env(path)

    cfg = Config(
        vk_bot=VkBot(
            token=env('BOT_TOKEN'),
            group_id=env('GROUP_ID')
        ),
        db=DataBaseConfig(
            db_name=env('DB_NAME'),
            db_host=env('DB_HOST'),
            db_user=env('DB_USER'),
            db_password=env('DB_PASSWORD')
        )
    )
    return cfg
