# Generated by Django 2.0 on 2020-02-13 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_user_is_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.CharField(default='', max_length=2),
        ),
    ]