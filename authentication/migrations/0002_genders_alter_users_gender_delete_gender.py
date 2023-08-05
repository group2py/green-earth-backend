# Generated by Django 4.2.4 on 2023-08-02 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name_plural': 'Genders',
            },
        ),
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='authentication.genders'),
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
    ]