# Generated by Django 5.2 on 2025-06-06 07:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Package', '0006_remove_package_senders_name'),
        ('Receipt', '0003_alter_receipt_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='package',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='receipts', to='Package.package'),
        ),
    ]
