from django.conf import settings
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

def send_email(path_template: str, assunto: str, para: list, **kwargs) -> dict:
    html = render_to_string(path_template, kwargs)
    text = strip_tags(html)

    emails = EmailMultiAlternatives(assunto, text, settings.EMAIL_HOST_USER, para)

    emails.attach_alternative(html, 'text/html')
    emails.send()
    return {'status': 'success'}