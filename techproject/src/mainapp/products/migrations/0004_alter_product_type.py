# Generated by Django 3.2.3 on 2021-07-25 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('appetizers', 'appetizers'), ('entrees', 'entrees'), ('treats', 'treats'), ('drinks', 'drinks')], max_length=60),
        ),
    ]
