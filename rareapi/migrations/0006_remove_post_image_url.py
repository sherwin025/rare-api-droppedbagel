# Generated by Django 4.0.2 on 2022-02-17 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0005_rename_game_postimage_post_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_url',
        ),
    ]
