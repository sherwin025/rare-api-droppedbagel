# Generated by Django 4.0.2 on 2022-02-16 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0002_reaction_postreaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='userPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(null=True, upload_to='profileimages')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='pictures', to='rareapi.theuser')),
            ],
        ),
    ]
