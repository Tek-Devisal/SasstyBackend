# Generated by Django 4.1 on 2022-08-31 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_categories_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
