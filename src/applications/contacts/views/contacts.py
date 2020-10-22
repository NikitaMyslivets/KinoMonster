from django.views.generic import TemplateView


class ContactsView(TemplateView):
    template_name = 'contacts/contact.html'