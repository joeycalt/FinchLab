# Generated by Django 4.1.1 on 2022-10-04 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_remove_toy_enjoy_toy_img_alter_dog_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('top', models.ManyToManyField(to='main_app.toy')),
            ],
        ),
    ]
