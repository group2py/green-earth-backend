from django.db import models
from authentication.models import Users

class CrimeDenunciations(models.Model):
    image = models.ImageField(upload_to='image_denunciations')
    user = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    description = models.TextField(max_length=500)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=80)
    number = models.IntegerField()
    reference_point = models.CharField(max_length=100)
    phone = models.IntegerField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = 'CrimeDenunciations'

class MediaOng(models.Model):
    image_before = models.ImageField(upload_to='images_ong')
    image_after = models.ImageField(upload_to='images_ong')
    title = models.CharField(max_length=150)
    owner = models.ForeignKey(Users, on_delete=models.DO_NOTHING)

    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.owner.username
    
    class Meta:
        verbose_name_plural = 'MediaOng'

class BlogPost(models.Model):
    image = models.ImageField(upload_to='image_blog')
    owner = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner.username
    
    class Meta:
        verbose_name_plural = 'BlogPost'
