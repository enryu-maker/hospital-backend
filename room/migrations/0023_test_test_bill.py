# Generated by Django 5.0.1 on 2024-02-04 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0022_patient_discharge'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='test_bill',
            field=models.FloatField(null=True),
        ),
    ]
