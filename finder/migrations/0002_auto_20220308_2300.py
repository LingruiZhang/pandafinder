# Generated by Django 2.1.5 on 2022-03-08 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='overall_rate',
            field=models.FloatField(null=True),
        ),
    ]