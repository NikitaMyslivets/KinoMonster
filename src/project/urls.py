from pathlib import Path

from django.contrib import admin
from django.http import HttpRequest
from django.http import HttpResponse
from django.urls import path
from django.urls import include




def view_index(request: HttpRequest):
    index_html = Path(__file__).parent.parent.parent / "static" / "index.html"
    with index_html.open(encoding='utf-8') as fp:
        content = fp.read()
    resp = HttpResponse(content, content_type="text/html", status=200)

    print(request)

    return resp


def view_logo(request: HttpRequest):
    logo = Path(__file__).parent.parent.parent / "static" / "img" / "cloud.png"
    with logo.open("rb") as fp:
        content = fp.read()
    return HttpResponse(content, content_type="image/png")


def view_css(request: HttpRequest):
    css_file = Path(__file__).parent.parent.parent / "static" / "styles" / "style.css"
    with css_file.open("r") as fp:
        content = fp.read()
    return HttpResponse(content, content_type="text/css")


urlpatterns = [
    path("", include('applications.home.urls')),
    path("admin/", admin.site.urls),
    path("i/cloud.png", view_logo),
    path("s/style.css", view_css),
    path("hello/", include('applications.hello.urls')),


]