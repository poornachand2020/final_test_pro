# Generated by Django 2.2.1 on 2020-01-23 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_auto_20200123_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='username',
            field=models.EmailField(max_length=30),
        ),
    ]