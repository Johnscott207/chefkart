# Generated by Django 4.0.4 on 2022-05-28 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_product_variant1_product_variant2_product_variant3_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='variant1',
            new_name='variant4_64gb',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='variant2',
            new_name='variant6_64gb',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='variant3',
            new_name='variant8_128gb',
        ),
        migrations.RemoveField(
            model_name='product',
            name='ram',
        ),
    ]
