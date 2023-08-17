from django.db import models
from authentication.models import Users

class Volunteers(models.Model):
    choices = (
        ('EA', 'Educação ambiental'),
        ('LAN', 'Limpeza e preservação de áreas naturais'),
        ('R', 'Reflorestamento e plantio de árvores'),
        ('RE', 'Reciclagem'),
        ('ER', 'Energias renováveis'),
        ('AS', 'Agricultura sustentável'),
        ('CA', 'Conservação da água'),
        ('MS', 'Mobilidade sustentável'),
        ('GR', 'Gestão de resíduos'),
        ('PVS', 'Proteção da vida selvagem'),
        ('AEP', 'Advocacia e engajamento político'),
        ('TS', 'Tecnologias sustentáveis'),
        ('ACL', 'Ações em comunidades locais'),
        ('MA', 'Monitoramento ambiental'),
        ('DC', 'Design e comunicação'),
    )

    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    help = models.CharField(max_length=70, choices=choices)
    
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = 'Volunteers'

class NewMission(models.Model):
    owner = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    volunteers = models.ManyToManyField(Volunteers, blank=True, null=True)
    concluded = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner.username
    
    class Meta:
        verbose_name_plural = 'NewMission'

class HistoryVoluntary(models.Model):
    voluntary = models.ForeignKey(Volunteers, on_delete=models.DO_NOTHING)
    mission = models.ForeignKey(NewMission, on_delete=models.DO_NOTHING)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    role = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.voluntary.user.username
    
    def save(self, *args, **kwargs):
        self.state = self.mission.state
        self.city = self.mission.city
        self.role = self.voluntary.help
        super(HistoryVoluntary, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'HistoryVoluntary'