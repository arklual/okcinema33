# Generated by Django 3.1.4 on 2021-02-19 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='serial',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Дата'),
        ),
    ]
