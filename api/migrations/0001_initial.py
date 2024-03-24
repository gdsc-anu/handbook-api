# Generated by Django 5.0.3 on 2024-03-24 01:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HandbookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='HandbookEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='content_images')),
                ('video', models.URLField(blank=True, null=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='content_images')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.handbookcategory')),
            ],
            options={
                'ordering': ['category', 'title'],
                'unique_together': {('category', 'title')},
            },
        ),
    ]
