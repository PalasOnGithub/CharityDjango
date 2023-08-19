from django.apps import AppConfig


class Part2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'part2'
    verbose_name = 'کارنامه ها و پرونده ها'

    def ready(self):
        import part2.signals


