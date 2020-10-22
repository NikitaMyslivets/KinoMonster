from django.apps import AppConfig


class ContactsConfig(AppConfig):
    label = 'contacts'
    name = f'applications.{label}'
