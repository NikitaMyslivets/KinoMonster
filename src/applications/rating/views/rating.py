from django.views.generic import TemplateView

class RatingView(TemplateView):
    template_name = 'rating/rating.html'