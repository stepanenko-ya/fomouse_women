# Generated by Django 4.2.6 on 2023-11-01 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('films', models.CharField(max_length=255, null=True, verbose_name='Film name')),
            ],
        ),
        migrations.CreateModel(
            name='Women',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('content', models.TextField(blank=True, verbose_name='Article text')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Photo')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True, verbose_name='Published')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='women.category', verbose_name='Category')),
                ('films', models.ManyToManyField(default=1, to='women.films')),
            ],
            options={
                'ordering': ['title', 'id'],
            },
        ),
    ]