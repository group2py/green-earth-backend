import os
from core import settings
from celery import shared_task
from authentication.models import Users
from .models import Volunteers, NewMission
from django.shortcuts import get_object_or_404

from .email import send_email

@shared_task(bind=True)
def notice_new_mission_volunteers(self, mission_id: int, volunteers: list):
    mission = get_object_or_404(NewMission, pk=mission_id)
    path_template = os.path.join(settings.BASE_DIR, 'blog/templates/emails/mission.html')
    for voluntary in volunteers:
        voluntary = get_object_or_404(Volunteers, pk=voluntary.id)
        send_email(path_template, f'New mission {mission.title}! To help the environment. Come join!', [voluntary.email,], username=voluntary.username, mission=mission)