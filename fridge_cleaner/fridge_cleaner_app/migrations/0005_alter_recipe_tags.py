# Generated by Django 3.2.7 on 2021-11-12 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fridge_cleaner_app', '0004_rename_tags_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(null=True, to='fridge_cleaner_app.Tag'),
        ),
    ]