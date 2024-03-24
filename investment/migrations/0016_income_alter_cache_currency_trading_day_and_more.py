# Generated by Django 5.0.1 on 2024-03-13 08:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("investment", "0015_alter_cache_currency_trading_day_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Income",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("catagories", models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name="cache_currency",
            name="trading_day",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 3, 13, 8, 18, 4, 454945, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="cache_stocks",
            name="trading_day",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 3, 13, 8, 18, 4, 453950, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="expenses_trackers",
            name="tracked_at",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 3, 13, 8, 18, 4, 455919, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
