# Generated by Django 3.2.10 on 2022-01-19 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='status',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
