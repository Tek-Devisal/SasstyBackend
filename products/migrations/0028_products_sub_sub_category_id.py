# Generated by Django 4.1 on 2022-11-23 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_products_img_4_products_img_5_products_img_6'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='sub_sub_category_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='products.subsubcategories'),
        ),
    ]
