from django.views.generic import TemplateView


class FilmsView(TemplateView):
    template_name = 'films/films.html'