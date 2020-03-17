# Generated by Django 3.0.3 on 2020-03-12 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webexample', '0012_auto_20200312_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default='2000-12-12'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default='2000-12-12'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='genre',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default='2000-12-12'),
            preserve_default=False,
        ),
    ]