# Generated by Django 3.2 on 2022-09-01 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0006_billing_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], max_length=255, null=True),
        ),
    ]
