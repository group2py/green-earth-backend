from django.db import models
from authentication.models import Users


class Volunteers(models.Model):
    choices = (
        ('educacao_ambiental', 'Educação ambiental'),
        ('limpeza_areas_naturais', 'Limpeza e preservação de áreas naturais'),
        ('reflorestamento', 'Reflorestamento e plantio de árvores'),
        ('reciclagem', 'Reciclagem'),
        ('energias_renovaveis', 'Energias renováveis'),
        ('agricultura_sustentavel', 'Agricultura sustentável'),
        ('conservacao_agua', 'Conservação da água'),
        ('mobilidade_sustentavel', 'Mobilidade sustentável'),
        ('gestao_residuos', 'Gestão de resíduos'),
        ('protecao_vida_selvagem', 'Proteção da vida selvagem'),
        ('advocacia_engajamento_politico', 'Advocacia e engajamento político'),
        ('tecnologias_sustentaveis', 'Tecnologias sustentáveis'),
        ('acoes_comunidades_locais', 'Ações em comunidades locais'),
        ('monitoramento_ambiental', 'Monitoramento ambiental'),
        ('design_comunicacao', 'Design e comunicação'),
    )

    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    help = models.CharField(max_length=70, choices=choices)
    
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    