# Generated by Django 4.2.2 on 2024-07-30 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_payments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='summ',
            field=models.PositiveIntegerField(default=10, verbose_name='сумма платежа'),
        ),
    ]
