# Generated by Django 4.0.5 on 2022-06-10 09:13

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('serials', '0004_alter_serial_kp_id'),
        ('films', '0013_alter_film_options_alter_genre_options_and_more'),
        ('marks', '0004_auto_20210502_1425'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filmrecension',
            options={'verbose_name': 'Рецензия фильма', 'verbose_name_plural': 'Рецензии фильмов'},
        ),
        migrations.AlterModelOptions(
            name='serialrecension',
            options={'verbose_name': 'Рецензия сериала', 'verbose_name_plural': 'Рецензии сериалов'},
        ),
        migrations.AlterField(
            model_name='filmrecension',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.film', verbose_name='Фильм'),
        ),
        migrations.AlterField(
            model_name='filmrecension',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='filmrecension',
            name='title',
            field=models.CharField(default='', max_length=120, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='filmrecension',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='serialrecension',
            name='serial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serials.serial', verbose_name='Сериал'),
        ),
        migrations.AlterField(
            model_name='serialrecension',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='serialrecension',
            name='title',
            field=models.CharField(default='', max_length=120, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='serialrecension',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]