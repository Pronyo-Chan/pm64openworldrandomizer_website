# Generated by Django 4.0.1 on 2022-01-25 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomizer', '0004_setting_includedojo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='InitialCoins',
            field=models.IntegerField(default=0),
        ),
    ]
