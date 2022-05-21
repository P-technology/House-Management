# Generated by Django 3.2.6 on 2022-05-14 13:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Agent', '0009_house_user_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='user_message',
            field=models.ManyToManyField(blank=True, related_name='user_message', to=settings.AUTH_USER_MODEL),
        ),
    ]