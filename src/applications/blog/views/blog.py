from django.views.generic import ListView

from applications.blog.models import Post


class BlogView(ListView):
    template_name = 'blog/blog.html'
    model = Post
    queryset = Post.objects.filter(visible=True)