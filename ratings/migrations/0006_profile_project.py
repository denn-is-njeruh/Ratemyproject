# Generated by Django 3.2.7 on 2021-09-27 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0005_project_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='',
            name='',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ratings.project'),
        ),
    ]
