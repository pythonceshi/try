# Generated by Django 3.0.3 on 2020-09-23 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysql02', '0008_auto_20200923_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='maninfo',
            name='off',
            field=models.IntegerField(default=0),
        ),
    ]
