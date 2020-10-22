from django.urls import path
from applications.contacts.views import ContactsView
from applications.contacts.apps import ContactsConfig


app_name = ContactsConfig.label

urlpatterns = [
    path('', ContactsView.as_view(), name='index'),

]