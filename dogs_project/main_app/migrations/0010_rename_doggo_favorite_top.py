# Generated by Django 4.1.1 on 2022-10-04 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_rename_top_favorite_doggo_favorite_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorite',
            old_name='doggo',
            new_name='top',
        ),
    ]
