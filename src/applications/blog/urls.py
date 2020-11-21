from django.urls import path
from applications.blog.views import BlogView, NewPostView, DeletePostView, EditPostView
from applications.blog.apps import BlogConfig
from applications.blog.views.post import PostView

app_name = BlogConfig.label

urlpatterns = [
    path('', BlogView.as_view(), name='index'),
    path('<int:pk>/', PostView.as_view(), name='post'),
    path('<int:pk>/delete/', DeletePostView.as_view(), name='delete-post'),
    path('<int:pk>/update/', EditPostView.as_view(), name='update-post'),
    path('new/', NewPostView.as_view(), name='new-post'),

]