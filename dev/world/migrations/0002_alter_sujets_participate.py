# Generated by Django 4.2.2 on 2023-08-01 19:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sujets',
            name='participate',
            field=models.ManyToManyField(blank=True, related_name='participate', to=settings.AUTH_USER_MODEL, verbose_name='Participants'),
        ),
    ]
