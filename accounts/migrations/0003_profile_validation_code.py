# Generated by Django 3.1.7 on 2021-04-09 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210404_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='validation_code',
            field=models.IntegerField(default=0),
        ),
    ]
