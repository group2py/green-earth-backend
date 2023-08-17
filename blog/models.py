from django.db import models
from authentication.models import Users
from volunteers.models import NewMission


class CrimeDenunciations(models.Model):
    image = models.ImageField(upload_to='image_denunciations', blank=True, null=True)
    user = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    description = models.TextField(max_length=500)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=80)
    number = models.IntegerField(blank=True, null=True)
    reference_point = models.CharField(max_length=100, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = 'CrimeDenunciations'

class MediaOng(models.Model):
    image_before = models.ImageField(upload_to='images_ong')
    image_after = models.ImageField(upload_to='images_ong', blank=True, null=True)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    owner = models.ForeignKey(Users, on_delete=models.DO_NOTHING)

    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.owner.username
    
    class Meta:
        verbose_name_plural = 'MediaOng'

class FinancialResources(models.Model):
    empresa = models.CharField(max_length=40, default='Ong Green Earth')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    value = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.empresa
    
    class Meta:
        verbose_name_plural = 'FinancialResources'

class BlogPost(models.Model):
    image = models.ImageField(upload_to='image_blog')
    owner = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    volunteers = models.ManyToManyField(NewMission, blank=True, null=True)
    public = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.owner.username
    
    class Meta:
        verbose_name_plural = 'BlogPost'

