from django.apps import AppConfig


class CalConfig(AppConfig):
    name = 'cal'
    verbose_name = 'Электронная регистрация'

from suit.apps import DjangoSuitConfig

class SuitConfig(DjangoSuitConfig):

        layout = 'horizontal'