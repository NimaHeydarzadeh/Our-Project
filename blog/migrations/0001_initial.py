# Generated by Django 4.0.4 on 2022-05-26 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.userprofile')),
                ('dislike', models.ManyToManyField(related_name='post_dislike', to='blog.userprofile')),
                ('like', models.ManyToManyField(related_name='post_like', to='blog.userprofile')),
            ],
        ),
    ]