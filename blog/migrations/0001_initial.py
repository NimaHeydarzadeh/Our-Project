# Generated by Django 4.0.4 on 2022-06-04 06:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messeges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('messege', models.TextField()),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_modify', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('bio', models.CharField(blank=True, max_length=200, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modify_date', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modify_date', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.userprofile')),
                ('dislike', models.ManyToManyField(blank=True, related_name='post_dislike', to='blog.userprofile')),
                ('like', models.ManyToManyField(related_name='post_like', to='blog.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_modify', models.DateTimeField(auto_now=True)),
                ('object_id', models.PositiveIntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.userprofile')),
                ('content_type', models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('dislike', models.ManyToManyField(blank=True, related_name='comment_dislikes', to='blog.userprofile')),
                ('like', models.ManyToManyField(blank=True, related_name='comment_likes', to='blog.userprofile')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post')),
            ],
        ),
    ]
