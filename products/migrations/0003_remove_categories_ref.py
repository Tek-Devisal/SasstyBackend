# Generated by Django 4.1 on 2022-08-31 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_categories_ref_alter_categories_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='ref',
        ),
    ]
