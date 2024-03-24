# Generated by Django 5.0.1 on 2024-03-12 17:07

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("investment", "0013_rename_expensise_expensive_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cache_currency",
            name="trading_day",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 3, 12, 17, 7, 34, 502222, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="cache_stocks",
            name="trading_day",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 3, 12, 17, 7, 34, 501196, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.CreateModel(
            name="Expensives_trackers",
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
                ("items", models.CharField(max_length=200)),
                ("price", models.IntegerField()),
                (
                    "tracked_at",
                    models.DateField(
                        default=datetime.datetime(
                            2024, 3, 12, 17, 7, 34, 502222, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
                (
                    "Catagories",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="investment.expensive",
                    ),
                ),
            ],
        ),
    ]
