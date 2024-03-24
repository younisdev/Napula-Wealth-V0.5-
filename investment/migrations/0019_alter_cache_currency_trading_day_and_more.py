# Generated by Django 5.0.1 on 2024-03-13 09:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("investment", "0018_rename_catagories_income_tracker_categories_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cache_currency",
            name="trading_day",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 3, 13, 9, 12, 51, 102293, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="cache_stocks",
            name="trading_day",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 3, 13, 9, 12, 51, 101079, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="expenses_trackers",
            name="tracked_at",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 3, 13, 9, 12, 51, 102293, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="income_tracker",
            name="tracked_at",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 3, 13, 9, 12, 51, 103082, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
