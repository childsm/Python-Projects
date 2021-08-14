# Generated by Django 3.2.3 on 2021-05-26 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='Prefix',
            field=models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms')], default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='First_Name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='Last_Name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
