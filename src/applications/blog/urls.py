from django.urls import path
from applications.blog.views import BlogView, NewPostView, DeletePostView, EditPostView
from applications.blog.apps import BlogConfig

app_name = BlogConfig.label

urlpatterns = [
    path('', BlogView.as_view(), name='index'),
    path('<int:pk>/delete/', DeletePostView.as_view(), name='delete-post'),
    path('<int:pk>/update/', EditPostView.as_view(), name='update-post'),
    path('new/', NewPostView.as_view(), name='new-post'),

]