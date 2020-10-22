from django.urls import path
from applications.films.views import FilmsView
from applications.films.apps import FilmsConfig

app_name = FilmsConfig.label

urlpatterns = [
    path('', FilmsView.as_view(), name='index')
]