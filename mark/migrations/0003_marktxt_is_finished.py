# Generated by Django 2.0 on 2020-03-07 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mark', '0002_remove_marktxt_c_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='marktxt',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
    ]
