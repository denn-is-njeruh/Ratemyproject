# Generated by Django 3.2.7 on 2021-09-27 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ratings', '0010_auto_20210927_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ratings.project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]