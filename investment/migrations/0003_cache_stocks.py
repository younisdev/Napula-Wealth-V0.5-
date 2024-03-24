# Generated by Django 5.0.1 on 2024-03-09 17:05

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("investment", "0002_rename_compnay_symbol_company"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cache_stocks",
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
                ("volume", models.IntegerField()),
                (
                    "trading_day",
                    models.DateField(
                        default=datetime.datetime(
                            2024, 3, 9, 17, 5, 55, 111174, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=12)),
                ("prev_price", models.DecimalField(decimal_places=2, max_digits=12)),
                (
                    "symbol",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="investment.symbol",
                    ),
                ),
            ],
        ),
    ]