# Generated by Django 4.1 on 2022-09-02 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("adminpanel", "0020_alter_billing_status_alter_customer_status_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Expense",
        ),
    ]