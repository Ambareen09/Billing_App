# Generated by Django 3.2 on 2022-09-01 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0007_vendor_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='phone_number',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
