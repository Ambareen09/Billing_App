# Generated by Django 3.2 on 2022-09-01 18:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0004_auto_20220901_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date_created',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]