# Generated by Django 4.0.4 on 2022-05-28 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_test_post_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default=1, max_length=140),
            preserve_default=False,
        ),
    ]
