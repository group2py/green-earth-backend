from django.db import models
from authentication.models import Users

class Contributors(models.Model):
    user = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    company = models.CharField(max_length=150)
    description = models.TextField(max_length=600)
    role = models.CharField(max_length=10, default='Financial')

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = 'Contributors'

class ContributionHistory(models.Model):
    user = models.ForeignKey(Contributors, on_delete=models.DO_NOTHING)#seria bom mudar o nome de user para contributor
    company = models.CharField(max_length=150)
    value = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.user.username
    
    class Meta:
        verbose_name_plural = 'ContributionHistory'
