# Generated by Django 4.2.2 on 2023-06-16 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_alter_type_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='system',
            name='img',
            field=models.ImageField(default='', upload_to='systems/logos/', verbose_name='صورة لوجو النظام'),
            preserve_default=False,
        ),
    ]
