# Generated by Django 2.0 on 2020-02-13 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_headman',
            field=models.BooleanField(default=False),
        ),
    ]