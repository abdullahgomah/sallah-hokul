# Generated by Django 4.2.2 on 2023-07-04 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0004_paypal_subscription'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paypal',
            options={'verbose_name': 'حساب باي بال', 'verbose_name_plural': 'حسابات باي بال'},
        ),
    ]