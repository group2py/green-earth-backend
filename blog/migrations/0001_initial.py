# Generated by Django 4.2.4 on 2023-08-17 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('volunteers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialResources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(default='Ong Green Earth', max_length=40)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('value', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'FinancialResources',
            },
        ),
        migrations.CreateModel(
            name='MediaOng',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_before', models.ImageField(upload_to='images_ong')),
                ('image_after', models.ImageField(blank=True, null=True, upload_to='images_ong')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'MediaOng',
            },
        ),
        migrations.CreateModel(
            name='CrimeDenunciations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image_denunciations')),
                ('description', models.TextField(max_length=500)),
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=80)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('reference_point', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'CrimeDenunciations',
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image_blog')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=500)),
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('public', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('volunteers', models.ManyToManyField(blank=True, null=True, to='volunteers.newmission')),
            ],
            options={
                'verbose_name_plural': 'BlogPost',
            },
        ),
    ]
