# Generated by Django 2.1.2 on 2018-11-17 16:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0016_progress'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='progress',
            unique_together={('user', 'resource')},
        ),
    ]