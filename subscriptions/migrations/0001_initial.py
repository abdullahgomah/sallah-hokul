# Generated by Django 4.2.2 on 2023-07-03 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='اسم الباقة')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='سعر الباقة (دولار)')),
            ],
            options={
                'verbose_name': 'باقة',
                'verbose_name_plural': 'باقات',
            },
        ),
    ]
