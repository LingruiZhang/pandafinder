# Generated by Django 4.0.3 on 2022-03-10 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0004_alter_category_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
    ]
