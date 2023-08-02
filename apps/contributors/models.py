from django.db import models
from authentication.models import Users

class Contributors(models.Model):
    user = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    company = models.CharField(max_length=150)
    description = models.TextField(max_length=600)
    role = models.CharField(max_length=10, default='Finanaceiro')

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = 'Contributors'

class ContributionHistory(models.Model):
    user = models.ForeignKey(Contributors, on_delete=models.DO_NOTHING)
    value = models.DecimalField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = 'ContributionHistory'
