# IMPORTS LIBRARIES PYTHON
from typing import Any

# IMPORTS DJANGO
from django.dispatch import receiver
from django.db.models.signals import post_save

# IMPORTS FILES OF APP
from .models import Users
from .activate_account import ActivateAccount

@receiver(post_save, sender=Users)
def activate_account_mail(sender: Users, instance: Users, created: Users, **kwargs: Any):
    if created and not instance.is_active:
        activate_account = ActivateAccount(instance)
        activate_account.activate_account_send_email()
        