# Generated by Django 4.1 on 2022-10-07 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_alter_categories_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='productstatus',
            options={'verbose_name': 'Product Status', 'verbose_name_plural': 'Product Status'},
        ),
        migrations.AlterModelOptions(
            name='subcategories',
            options={'verbose_name': 'Sub Category', 'verbose_name_plural': 'Sub Categories'},
        ),
        migrations.RemoveField(
            model_name='stock',
            name='prize',
        ),
        migrations.AlterField(
            model_name='products',
            name='status',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='products.productstatus'),
        ),
    ]