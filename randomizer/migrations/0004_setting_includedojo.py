# Generated by Django 4.0.1 on 2022-01-24 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomizer', '0003_setting_isdefault'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='IncludeDojo',
            field=models.BooleanField(default=False),
        ),
    ]