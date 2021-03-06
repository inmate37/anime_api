# Generated by Django 4.0 on 2022-04-23 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='время обновления')),
                ('datetime_deleted', models.DateTimeField(blank=True, null=True, verbose_name='время удаления')),
                ('studio', models.CharField(default='', max_length=100, verbose_name='студия')),
                ('rating', models.IntegerField(verbose_name='рейтинг')),
            ],
            options={
                'verbose_name': 'аниме',
                'verbose_name_plural': 'аниме',
                'ordering': ('-datetime_created',),
            },
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_en', models.TextField(default='', verbose_name='текст на английском')),
                ('text_ru', models.TextField(default='', verbose_name='текст на русском')),
            ],
            options={
                'verbose_name': 'описание',
                'verbose_name_plural': 'описания',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='ReleaseDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.CharField(max_length=20, verbose_name='выпущен')),
                ('date', models.DateTimeField(verbose_name='дата')),
            ],
            options={
                'verbose_name': 'дата выпуска ',
                'verbose_name_plural': 'даты выпуска ',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='имя')),
                ('link', models.TextField(verbose_name='ссылка')),
            ],
            options={
                'verbose_name': 'дата выпуска',
                'verbose_name_plural': 'даты выпуска',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='имя')),
                ('anime', models.ManyToManyField(related_name='genres', to='anime.Anime', verbose_name='аниме')),
            ],
            options={
                'verbose_name': 'жанр',
                'verbose_name_plural': 'жанры',
                'ordering': ('-id',),
            },
        ),
        migrations.AddField(
            model_name='anime',
            name='description',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='anime.description', verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='anime',
            name='release_date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='anime.releasedate', verbose_name='дата выпуска'),
        ),
        migrations.AddField(
            model_name='anime',
            name='title',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='anime.title', verbose_name='название'),
        ),
    ]
