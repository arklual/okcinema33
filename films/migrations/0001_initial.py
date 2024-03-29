# Generated by Django 3.1.4 on 2021-02-19 15:54

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
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now=True)),
                ('description', models.TextField()),
                ('video', models.FileField(blank=True, null=True, upload_to='')),
                ('poster', models.FileField(blank=True, null=True, upload_to='')),
                ('raiting', models.FloatField(blank=True, default=0, null=True)),
                ('numMarks', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Serial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('date', models.DateField(auto_now=True)),
                ('description', models.TextField(default='')),
                ('count_sesonov', models.IntegerField(default=1)),
                ('poster', models.FileField(blank=True, null=True, upload_to='')),
                ('raiting', models.FloatField(blank=True, default=0, null=True)),
                ('numMarks', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.film')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Seriya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('number', models.IntegerField()),
                ('season', models.IntegerField()),
                ('video', models.FileField(blank=True, null=True, upload_to='')),
                ('serial', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='films.serial')),
            ],
        ),
        migrations.CreateModel(
            name='SerialVoter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.serial')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
