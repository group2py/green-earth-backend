from __future__ import absolute_import, unicode_literals 
import os 
from celery import Celery 
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings') 

app = Celery('core') 
app.config_from_object('django.conf:settings', namespace='CELERY') 

app.conf.enable_utc = False

app.conf.beat_schedule = {
    'send-email-marketing-every-sunday': {
        'task': 'blog.tasks.send_mail_to_general',
        'schedule': crontab(0, 0, day_of_month='2'),
        'args' : ("Success",)
    }
}

app.conf.update(timezone = 'America/Sao_Paulo') 

app.autodiscover_tasks()