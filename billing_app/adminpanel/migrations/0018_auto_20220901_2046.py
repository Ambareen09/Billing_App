# Generated by Django 3.2 on 2022-09-01 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0017_auto_20220901_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminpanel.staff'),
        ),
        migrations.AlterField(
            model_name='billing',
            name='status',
            field=models.CharField(choices=[('PAID', 'PAID'), ('UNPAID', 'UNPAID')], max_length=255, null=True),
        ),
    ]
