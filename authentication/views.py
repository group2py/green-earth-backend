from django.shortcuts import render, get_object_or_404
import os
from authentication.models import Users
# Create your views here.
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def send_email(path_template: str, assunto: str, para: list, **kwargs) -> dict:
    html = render_to_string(path_template, kwargs)
    text = strip_tags(html)

    emails = EmailMultiAlternatives(assunto, text, settings.EMAIL_HOST_USER, para)

    emails.attach_alternative(html, 'text/html')
    emails.send()
    return {'status': 1}

def t(request):
    user = get_object_or_404(Users, pk=request.user.pk)
    path_template = os.path.join(settings.BASE_DIR, 'authentication/templates/emails/marketing.html')
    send_email(path_template, f"Hello {user.username}, Do you need to study programming?", [user.email,])
    return render(request, 'emails/marketing.html')