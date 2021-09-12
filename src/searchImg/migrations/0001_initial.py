# Generated by Django 3.2.7 on 2021-09-12 02:50

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('characteristics', django_mysql.models.ListCharField(models.CharField(max_length=12), max_length=78, size=6)),
                ('description', models.TextField(default='cool')),
                ('price', models.TextField(default=0)),
            ],
        ),
    ]
