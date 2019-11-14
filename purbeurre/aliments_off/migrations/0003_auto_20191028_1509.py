# Generated by Django 2.2.6 on 2019-10-28 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aliments_off', '0002_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='id_product',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='SaveProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aliments_off.Products')),
            ],
        ),
    ]
