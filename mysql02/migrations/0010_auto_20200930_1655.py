# Generated by Django 3.0.3 on 2020-09-30 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysql02', '0009_maninfo_off'),
    ]

    operations = [
        migrations.AddField(
            model_name='maninfo',
            name='admin',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='maninfo',
            name='change',
            field=models.IntegerField(default=0),
        ),
    ]
