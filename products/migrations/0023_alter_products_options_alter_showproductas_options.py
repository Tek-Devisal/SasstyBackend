# Generated by Django 4.1 on 2022-10-08 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_delete_stock'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='showproductas',
            options={'verbose_name': 'Show Product As', 'verbose_name_plural': 'Show Products As'},
        ),
    ]
