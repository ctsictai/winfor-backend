# Generated by Django 2.2.6 on 2019-11-07 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('champion_infos', '0002_auto_20191107_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='champ_info',
            name='story',
            field=models.TextField(max_length=500),
        ),
    ]
