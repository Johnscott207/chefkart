# Generated by Django 4.0.4 on 2022-05-28 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_rename_product_id_product_variant_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_variant',
            name='color',
            field=models.CharField(choices=[('Red', 'Red'), ('Blue', 'Blue'), ('Green', 'Green')], default='1', max_length=9),
        ),
        migrations.AlterField(
            model_name='product_variant',
            name='variant',
            field=models.CharField(choices=[('4gb 64gb', '4gb 64gb'), ('6gb 64gb', '6gb 64gb'), ('8gb 128gb', '8gb 128gb')], default='1', max_length=9),
        ),
    ]