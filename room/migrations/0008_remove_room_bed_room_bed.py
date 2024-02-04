# Generated by Django 5.0.1 on 2024-02-04 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0007_rename_bed_room_bed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='bed',
        ),
        migrations.AddField(
            model_name='room',
            name='bed',
            field=models.ManyToManyField(blank=True, null=True, to='room.bed'),
        ),
    ]
