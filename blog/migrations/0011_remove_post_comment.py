# Generated by Django 4.0.4 on 2022-06-01 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_rename_auther_comment_author_rename_auth_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment',
        ),
    ]
