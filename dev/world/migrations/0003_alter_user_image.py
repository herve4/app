# Generated by Django 4.2.2 on 2023-08-01 20:35

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_alter_sujets_participate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default='media/2.jpg', error_messages='Seule les images sont autorisées', force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[270, 250], upload_to='media/'),
        ),
    ]