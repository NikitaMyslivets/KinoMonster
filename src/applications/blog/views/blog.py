from django.views.generic import TemplateView

from applications.blog.models import Post


class BlogView(TemplateView):
    template_name = 'blog/blog.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx['object_list'] = Post.objects.filter(visible=True)
        return ctx