# Generated by Django 3.1.7 on 2021-04-08 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0007_auto_20210408_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='film',
            field=models.ManyToManyField(blank=True, to='films.Film'),
        ),
    ]
