# Generated by Django 4.0.4 on 2022-05-28 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_remove_product_color_remove_product_variant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('1', 'Red'), ('2', 'Blue'), ('3', 'Green')], default='1', max_length=9)),
                ('variant', models.CharField(choices=[('1', '4gb 64gb'), ('2', '6gb 64gb'), ('3', '8gb 128gb')], default='1', max_length=9)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
        ),
    ]