# Generated by Django 3.2.13 on 2022-09-30 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='star',
            field=models.FloatField(default=1.0),
        ),
    ]