# Generated by Django 5.2 on 2025-05-14 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Package', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='dimensions',
        ),
        migrations.AddField(
            model_name='package',
            name='height',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='package',
            name='length',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='package',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
