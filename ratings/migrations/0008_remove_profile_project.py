# Generated by Django 3.2.7 on 2021-09-27 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0007_alter_profile_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='project',
        ),
    ]