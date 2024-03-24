# Generated by Django 5.0.1 on 2024-03-11 21:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("investment", "0012_expensise_alter_cache_currency_trading_day_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Expensise",
            new_name="Expensive",
        ),
        migrations.AlterField(
            model_name="cache_currency",
            name="trading_day",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 3, 11, 21, 13, 57, 610694, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="cache_stocks",
            name="trading_day",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 3, 11, 21, 13, 57, 610694, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
