# Generated by Django 2.2.6 on 2019-11-03 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20191030_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='summoner_id',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='account',
            name='summoner_name',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]