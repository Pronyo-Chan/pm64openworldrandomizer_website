# Generated by Django 4.0.1 on 2022-01-24 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomizer_server', '0002_rename_blue_house_open_setting_allowphysicsglitches_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='IsDefault',
            field=models.BooleanField(default=False),
        ),
    ]