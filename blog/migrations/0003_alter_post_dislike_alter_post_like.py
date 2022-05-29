# Generated by Django 4.0.4 on 2022-05-29 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_create_date_post_modify_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dislike',
            field=models.ManyToManyField(null=True, related_name='post_dislike', to='blog.userprofile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(null=True, related_name='post_like', to='blog.userprofile'),
        ),
    ]
