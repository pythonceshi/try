# Generated by Django 3.0.3 on 2020-09-23 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysql02', '0003_maninfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maninfo',
            old_name='name',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='maninfo',
            old_name='num',
            new_name='usernum',
        ),
    ]
