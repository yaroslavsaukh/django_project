# Generated by Django 3.2.4 on 2021-06-16 13:47

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name="Ім'я")),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Вік')),
                ('description', models.TextField(verbose_name='Опис')),
                ('image', models.ImageField(upload_to='actors/', verbose_name='Зображення')),
            ],
            options={
                'verbose_name': 'Актори та режисери',
                'verbose_name_plural': 'Актори та режисери',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категорія')),
                ('description', models.TextField(verbose_name='Опис')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категорія',
                'verbose_name_plural': 'Категорії',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name="Ім'я")),
                ('description', models.TextField(verbose_name='Опис')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанри',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Назва')),
                ('tagline', models.CharField(default='', max_length=100, verbose_name='Слоган')),
                ('description', models.TextField(verbose_name='Опис')),
                ('poster', models.ImageField(upload_to='movies/', verbose_name='Постер')),
                ('year', models.PositiveSmallIntegerField(default=2021, verbose_name='Дата виходу')),
                ('country', models.CharField(max_length=30, verbose_name='Країна')),
                ('world_premiere', models.DateField(default=datetime.date.today, verbose_name="Прем'єра у світі")),
                ('budget', models.PositiveIntegerField(default=0, help_text='Сума в доларах', verbose_name='Бюджет')),
                ('fees_in_usa', models.PositiveIntegerField(default=0, help_text='Сума в доларах', verbose_name='Збори в США')),
                ('fees_in_world', models.PositiveIntegerField(default=0, help_text='Сума в доларах', verbose_name='Збори у світі')),
                ('url', models.SlugField(max_length=130, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Чернетка')),
                ('actors', models.ManyToManyField(related_name='film_actor', to='movies.Actor', verbose_name='актори')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.category', verbose_name='Категорія')),
                ('directors', models.ManyToManyField(related_name='film_director', to='movies.Actor', verbose_name='режисер')),
                ('genres', models.ManyToManyField(to='movies.Genre', verbose_name='жанри')),
            ],
            options={
                'verbose_name': 'Фільм',
                'verbose_name_plural': 'Фільми',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Значення')),
            ],
            options={
                'verbose_name': 'Зірка рейтингу',
                'verbose_name_plural': 'Зірки рейтингу',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name="Ім'я")),
                ('text', models.TextField(max_length=5000, verbose_name='Відгук')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie', verbose_name='фільм')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.reviews', verbose_name='Батько')),
            ],
            options={
                'verbose_name': 'Відгук',
                'verbose_name_plural': 'Відгуки',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP адреса')),
                ('movie', models.ForeignKey(on_delete=django.db.models.fields.CharField, to='movies.movie', verbose_name='фільм')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.ratingstar', verbose_name='зірка')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
        migrations.CreateModel(
            name='MovieShots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Опис')),
                ('image', models.ImageField(upload_to='movie_shots/', verbose_name='Зображення')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie', verbose_name='Фільм')),
            ],
            options={
                'verbose_name': 'Кадр з фільму',
                'verbose_name_plural': 'Кадри з фільму',
            },
        ),
    ]
