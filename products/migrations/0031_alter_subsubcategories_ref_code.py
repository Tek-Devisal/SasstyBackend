# Generated by Django 4.1 on 2022-12-16 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_alter_subsubcategories_ref_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsubcategories',
            name='ref_code',
            field=models.CharField(default='PWIG1L9Y', max_length=500),
        ),
    ]
