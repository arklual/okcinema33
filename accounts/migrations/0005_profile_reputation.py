# Generated by Django 3.1.7 on 2021-05-26 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210420_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='reputation',
            field=models.IntegerField(default=0),
        ),
    ]
