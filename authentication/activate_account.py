from django.urls import reverse
from django.conf import settings
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator

from .models import Users

class ActivateAccount:
    def __init__(self, user: Users):
        if not isinstance(user, Users):
            raise ValueError('User must be an instance of Users')        
        self._user = user

    def _generate_url(self) -> str:
        protocol = 'http' if settings.DEBUG else 'https'
        domain = settings.DOMAIN
        uid = urlsafe_base64_encode(force_bytes(self._user.pk))
        token = default_token_generator.make_token(self._user)

        return f"{protocol}://{domain}{reverse('activate_account', kwargs={'uid4': uid, 'token': token})}"
    
    def activate_account_send_email(self):
        activate_url = self._generate_url()
        subject = "Activate your account on Ong's | Environment"
        email_body = render_to_string('emails/activate_account.html', {'activate_url': activate_url})
        email_html = strip_tags(email_body)
        email = EmailMultiAlternatives(subject, email_html, settings.EMAIL_HOST_USER, to=[self._user.email])
        email.attach_alternative(email_body, 'text/html')
        print('3')
        email.send()
