# Generated by Django 4.0.4 on 2022-05-31 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_alter_post_slug_alter_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='title',
            field=models.CharField(default='title', max_length=150),
        ),
    ]
