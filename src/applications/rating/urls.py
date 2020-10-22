from django.urls import path

from applications.rating.views import RatingView
from applications.rating.apps import RatingConfig

app_name = RatingConfig.label

urlpatterns = [
    path('', RatingView.as_view(), name='index'),
]