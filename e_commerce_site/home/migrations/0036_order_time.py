# Generated by Django 4.0.4 on 2022-05-28 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_order_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]
