# Generated by Django 3.2.7 on 2021-09-15 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchImg', '0003_alter_img_image_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='img',
            name='discount',
            field=models.IntegerField(default=0),
        ),
    ]
