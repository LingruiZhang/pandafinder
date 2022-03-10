# Generated by Django 2.1.5 on 2022-02-26 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.CharField(max_length=20, unique=True)),
                ('content', models.TextField(default='')),
                ('rate', models.FloatField(default=0)),
                ('user_id', models.CharField(max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_id', models.CharField(max_length=20, unique=True)),
                ('r_name', models.CharField(max_length=30)),
                ('postcode', models.CharField(max_length=6)),
                ('address', models.CharField(max_length=100)),
                ('r_phone_num', models.CharField(max_length=10)),
                ('r_email', models.CharField(max_length=30)),
                ('website_url', models.URLField()),
                ('menu', models.ImageField(upload_to='')),
                ('photo', models.ImageField(upload_to='')),
                ('overall_rate', models.FloatField()),
                ('category', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finder.Restaurant'),
        ),
    ]
