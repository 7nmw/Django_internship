# Generated by Django 4.1.5 on 2023-01-07 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pereval_areas',
            name='id_parent',
            field=models.TextField(default=0, max_length=4),
        ),
    ]
