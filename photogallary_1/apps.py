from django.apps import AppConfig


class Photogallary1Config(AppConfig):
    name = 'photogallary_1'

def ready(self):
        import photogallary_1.signals