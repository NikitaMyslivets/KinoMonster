from django.core.mail import send_mail


def send(user_mail):
    send_mail(
        'hello',
        'hello',
        'hello',
        [user_mail],
        fail_silently=False,
    )