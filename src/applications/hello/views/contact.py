from django.views.generic import CreateView

from applications.hello.forms import ContactForm
from applications.hello.models import Contact
from applications.hello.service import send


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'hello/contact.html'

    def form_valid(self, form):
        form.save()
        send(form.instance.email)
        return super().form_valid(form)