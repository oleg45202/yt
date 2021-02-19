from django.apps import AppConfig

from .companies_redis import RedisClient


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        RedisClient().set_init_data()
