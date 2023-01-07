# Generated by Django 4.1.5 on 2023-01-07 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0004_alter_users_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pereval_added',
            name='autumn',
            field=models.TextField(blank=True, choices=[('1А', '1А'), ('1Б', '1Б'), ('2А', '2А'), ('2Б', '2Б'), ('3А', '3А'), ('3Б', '3Б')], max_length=5),
        ),
        migrations.AlterField(
            model_name='pereval_added',
            name='spring',
            field=models.TextField(blank=True, choices=[('1А', '1А'), ('1Б', '1Б'), ('2А', '2А'), ('2Б', '2Б'), ('3А', '3А'), ('3Б', '3Б')], max_length=5),
        ),
        migrations.AlterField(
            model_name='pereval_added',
            name='summer',
            field=models.TextField(blank=True, choices=[('1А', '1А'), ('1Б', '1Б'), ('2А', '2А'), ('2Б', '2Б'), ('3А', '3А'), ('3Б', '3Б')], max_length=5),
        ),
        migrations.AlterField(
            model_name='pereval_added',
            name='winter',
            field=models.TextField(blank=True, choices=[('1А', '1А'), ('1Б', '1Б'), ('2А', '2А'), ('2Б', '2Б'), ('3А', '3А'), ('3Б', '3Б')], max_length=5),
        ),
    ]
