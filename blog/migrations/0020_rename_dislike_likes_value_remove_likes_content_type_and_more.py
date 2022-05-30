# Generated by Django 4.0.4 on 2022-05-30 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_likes_dislikes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likes',
            old_name='dislike',
            new_name='value',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='date_create',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='date_modify',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='like',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='object_id',
        ),
        migrations.DeleteModel(
            name='dislikes',
        ),
    ]