# Generated by Django 3.1.4 on 2021-02-21 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('date', models.DateField(verbose_name='Дата')),
                ('description', models.TextField(default='')),
                ('count_sesonov', models.IntegerField(default=1)),
                ('poster', models.FileField(blank=True, null=True, upload_to='')),
                ('raiting', models.FloatField(blank=True, default=0, null=True)),
                ('numMarks', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seriya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.IntegerField()),
                ('number', models.IntegerField()),
                ('title', models.CharField(default='', max_length=50)),
                ('video', models.FileField(blank=True, null=True, upload_to='')),
                ('serial', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='serials.serial')),
            ],
        ),
    ]
