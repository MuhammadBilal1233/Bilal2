# Generated by Django 4.0.1 on 2022-04-06 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0005_alter_destination1_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination1',
            name='phone',
            field=models.IntegerField(verbose_name=1000000000),
        ),
    ]
