# Generated by Django 3.2.7 on 2021-09-26 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0004_auto_20210926_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='rating',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ratings.rating'),
        ),
    ]
