from celery import shared_task
from django.core.mail import EmailMessage


@shared_task
def send_to_email_task(subject, message, _email):
    email = EmailMessage(subject, message, to=[_email])
    email.content_subtype = 'html'
    email.send()
    return {'status': 'yuborildi', "email": _email}
