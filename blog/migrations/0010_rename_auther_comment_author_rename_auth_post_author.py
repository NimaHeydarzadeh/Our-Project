# Generated by Django 4.0.4 on 2022-06-01 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_rename_comment_body_comment_body_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='auther',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='auth',
            new_name='author',
        ),
    ]