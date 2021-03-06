# Generated by Django 2.2.3 on 2019-09-29 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_playlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='playlist',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='playlist',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
