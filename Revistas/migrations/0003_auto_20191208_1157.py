# Generated by Django 2.2.6 on 2019-12-08 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Revistas', '0002_auto_20191208_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticias',
            name='autor',
        ),
        migrations.AddField(
            model_name='noticias',
            name='id_autor',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='noticias',
            name='nome_autor',
            field=models.CharField(default='Not Found', max_length=100),
        ),
    ]