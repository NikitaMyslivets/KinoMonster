from django.urls import path
from applications.blog.views import BlogView
from applications.blog.apps import BlogConfig

app_name = BlogConfig.label

urlpatterns = [
    path('', BlogView.as_view(), name='index')
]