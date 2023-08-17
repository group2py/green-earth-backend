import os
from core import settings
from celery import shared_task
from authentication.models import Users
from volunteers.models import Volunteers
from django.shortcuts import get_object_or_404

from .email import send_email

@shared_task(bind=True)
def send_mail_to_general():
    users = Users.objects.all()
    for user in users:
        path_template = os.path.join(settings.BASE_DIR, 'blog/templates/emails/marketing.html')
        send_email(path_template, 'Ong Green Earth Come help the environment', [user.email,], username=user.username)
