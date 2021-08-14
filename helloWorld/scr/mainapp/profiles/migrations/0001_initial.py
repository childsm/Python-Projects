# Generated by Django 3.2.3 on 2021-05-26 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(blank=True, default='', max_length=30)),
                ('Last_Name', models.CharField(blank=True, default='', max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Username', models.CharField(blank=True, default='', max_length=60)),
            ],
        ),
    ]
