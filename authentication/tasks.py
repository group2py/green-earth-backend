from celery import shared_task 
from django.core.mail import send_mail 
from core import settings

@shared_task(bind=True) 
def send_notification_mail (self, target_mail, message): 
    mail_subject = "Bem-vindo a bordo!" 
    send_mail( 
        subject = mail_subject, 
        message=message, 
        from_email=settings.EMAIL_HOST_USER, 
        receiver_list=[target_mail], 
        fail_silently= False , 
        ) 
    return "Feito"