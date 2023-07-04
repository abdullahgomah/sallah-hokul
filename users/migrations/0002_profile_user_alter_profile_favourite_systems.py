# Generated by Django 4.2.2 on 2023-06-24 23:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0005_system_overview'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='المستخدم'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='favourite_systems',
            field=models.ManyToManyField(related_name='profiles', to='system.system', verbose_name='التقنيات المفضلة'),
        ),
    ]