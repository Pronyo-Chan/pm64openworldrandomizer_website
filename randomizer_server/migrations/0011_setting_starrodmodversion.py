# Generated by Django 4.0.1 on 2022-02-04 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomizer_server', '0010_setting_creationdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='StarRodModVersion',
            field=models.IntegerField(default=1),
        ),
    ]
