# Generated by Django 4.1 on 2022-08-31 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_categories_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
