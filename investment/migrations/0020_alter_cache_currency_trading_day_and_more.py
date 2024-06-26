# Generated by Django 5.0.1 on 2024-03-14 18:57

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("investment", "0019_alter_cache_currency_trading_day_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cache_currency",
            name="trading_day",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 3, 14, 18, 56, 59, 670521, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="cache_stocks",
            name="trading_day",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 3, 14, 18, 56, 59, 669520, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="expenses_trackers",
            name="tracked_at",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 3, 14, 18, 56, 59, 670521, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="income_tracker",
            name="tracked_at",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 3, 14, 18, 56, 59, 671595, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.CreateModel(
            name="Goals",
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
                ("budget", models.IntegerField()),
                (
                    "date",
                    models.DateField(
                        default=datetime.datetime(
                            2024,
                            3,
                            14,
                            18,
                            56,
                            59,
                            671595,
                            tzinfo=datetime.timezone.utc,
                        )
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
