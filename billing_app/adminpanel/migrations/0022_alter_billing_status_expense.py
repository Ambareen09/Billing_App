# Generated by Django 4.1 on 2022-09-02 17:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("adminpanel", "0021_delete_expense"),
    ]

    operations = [
        migrations.AlterField(
            model_name="billing",
            name="status",
            field=models.CharField(
                choices=[("UNPAID", "UNPAID"), ("PAID", "PAID")],
                max_length=255,
                null=True,
            ),
        ),
        migrations.CreateModel(
            name="Expense",
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
                ("created_on", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_on", models.DateTimeField(auto_now=True, null=True)),
                ("vendor", models.CharField(blank=True, max_length=256, null=True)),
                (
                    "date_created",
                    models.DateTimeField(
                        blank=True, default=django.utils.timezone.now, null=True
                    ),
                ),
                ("amount", models.FloatField(blank=True, null=True)),
                ("notes", models.TextField(blank=True, null=True)),
                (
                    "expense_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="expense_type",
                        to="adminpanel.expensetype",
                    ),
                ),
                (
                    "payment_mode",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payment_mode",
                        to="adminpanel.paymode",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
