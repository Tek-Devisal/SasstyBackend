# Generated by Django 4.1 on 2022-09-04 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_rename_category_subcategories_category_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_id', models.IntegerField(max_length=50)),
                ('show_for', models.IntegerField(max_length=50)),
                ('status', models.IntegerField(max_length=5)),
                ('category_id', models.IntegerField(max_length=50)),
                ('sub_category_id', models.IntegerField(max_length=50)),
                ('name', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=1000)),
                ('prize', models.FloatField(max_length=50)),
                ('discount', models.IntegerField(max_length=50)),
                ('img_1', models.CharField(max_length=50)),
                ('img_2', models.CharField(max_length=50)),
                ('img_3', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(max_length=50)),
                ('quantity', models.IntegerField(max_length=50)),
            ],
        ),
    ]
