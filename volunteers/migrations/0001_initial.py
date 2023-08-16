# Generated by Django 4.2.3 on 2023-08-15 22:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('help', models.CharField(choices=[('educacao_ambiental', 'Educação ambiental'), ('limpeza_areas_naturais', 'Limpeza e preservação de áreas naturais'), ('reflorestamento', 'Reflorestamento e plantio de árvores'), ('reciclagem', 'Reciclagem'), ('energias_renovaveis', 'Energias renováveis'), ('agricultura_sustentavel', 'Agricultura sustentável'), ('conservacao_agua', 'Conservação da água'), ('mobilidade_sustentavel', 'Mobilidade sustentável'), ('gestao_residuos', 'Gestão de resíduos'), ('protecao_vida_selvagem', 'Proteção da vida selvagem'), ('advocacia_engajamento_politico', 'Advocacia e engajamento político'), ('tecnologias_sustentaveis', 'Tecnologias sustentáveis'), ('acoes_comunidades_locais', 'Ações em comunidades locais'), ('monitoramento_ambiental', 'Monitoramento ambiental'), ('design_comunicacao', 'Design e comunicação')], max_length=70)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]