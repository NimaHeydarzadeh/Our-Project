# Generated by Django 4.0.4 on 2022-05-29 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment_content_type_comment_object_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
