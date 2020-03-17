# Generated by Django 3.0.3 on 2020-03-03 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webexample', '0002_book_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(default=144, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookorder',
            name='slug',
            field=models.SlugField(default=144, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='genre',
            name='slug',
            field=models.SlugField(default=144, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='slug',
            field=models.SlugField(default=111, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='recom_ages',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='RecomAge',
        ),
    ]
