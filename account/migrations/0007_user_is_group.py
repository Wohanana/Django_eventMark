# Generated by Django 2.0 on 2020-02-13 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20200213_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_group',
            field=models.BooleanField(default=False),
        ),
    ]
