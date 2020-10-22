from django.contrib import admin
from django.urls import path
from django.urls import include


def trigger_error(request):
    devision_by_zero = 1 / 0


urlpatterns = [
    path("", include('applications.home.urls')),
    path("admin/", admin.site.urls),
    path("hello/", include('applications.hello.urls')),
    path('contact/', include('applications.contacts.urls')),
    path('films/', include('applications.films.urls')),
    path('rating/', include('applications.rating.urls')),

    path('sentry-debug/', trigger_error),

]