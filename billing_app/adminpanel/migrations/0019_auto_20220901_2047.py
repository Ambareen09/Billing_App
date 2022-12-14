# Generated by Django 3.2 on 2022-09-01 20:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0018_auto_20220901_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='status',
            field=models.CharField(choices=[('UNPAID', 'UNPAID'), ('PAID', 'PAID')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='status',
            field=models.CharField(choices=[('INACTIVE', 'INACTIVE'), ('ACTIVE', 'ACTIVE')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='salary',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='status',
            field=models.CharField(choices=[('INACTIVE', 'INACTIVE'), ('ACTIVE', 'ACTIVE')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='status',
            field=models.CharField(choices=[('INACTIVE', 'INACTIVE'), ('ACTIVE', 'ACTIVE')], max_length=255, null=True),
        ),
    ]
