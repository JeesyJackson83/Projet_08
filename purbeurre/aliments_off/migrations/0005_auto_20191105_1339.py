# Generated by Django 2.2.6 on 2019-11-05 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aliments_off', '0004_products_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category_name',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
