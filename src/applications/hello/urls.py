from django.urls import path
from applications.hello.views import GreetView, ContactView
from applications.hello.views import ResetView
from applications.hello.apps import HelloConfig


app_name = HelloConfig.label

urlpatterns = [
    path('', GreetView.as_view(), name='index'),
    path('update/', GreetView.as_view(), name='update'),
    path('reset/', ResetView.as_view(), name='reset'),
    path('contact/', ContactView.as_view(), name='contact')
]