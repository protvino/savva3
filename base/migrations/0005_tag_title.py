# Generated by Django 2.1.2 on 2018-10-26 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20181026_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]