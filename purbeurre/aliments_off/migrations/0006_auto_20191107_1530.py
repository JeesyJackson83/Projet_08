# Generated by Django 2.2.6 on 2019-11-07 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aliments_off', '0005_auto_20191105_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='ingredients',
        ),
        migrations.RemoveField(
            model_name='products',
            name='purchase_place',
        ),
        migrations.AddField(
            model_name='products',
            name='fat',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='fat_100g',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='salt',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='salt_100g',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='saturated_fat',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='saturated_fat_100g',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='sugars',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='sugars_100g',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='saveproducts',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='products',
            name='img_url',
            field=models.URLField(),
        ),
    ]
