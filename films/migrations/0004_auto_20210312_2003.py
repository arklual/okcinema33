# Generated by Django 3.1.4 on 2021-03-12 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_auto_20210221_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='video',
            field=models.URLField(blank=True, null=True),
        ),
    ]
