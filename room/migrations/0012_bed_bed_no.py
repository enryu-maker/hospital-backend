# Generated by Django 5.0.1 on 2024-02-04 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0011_room_room_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='bed',
            name='bed_no',
            field=models.IntegerField(null=True),
        ),
    ]
