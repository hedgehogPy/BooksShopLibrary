# Generated by Django 3.0.3 on 2020-03-10 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webexample', '0009_auto_20200310_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='genre',
            name='photo',
            field=models.CharField(max_length=500),
        ),
    ]