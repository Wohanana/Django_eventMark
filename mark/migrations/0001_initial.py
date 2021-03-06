# Generated by Django 2.0 on 2020-02-19 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marktxt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marktxt_type', models.CharField(default='', max_length=50)),
                ('start', models.CharField(default='', max_length=10)),
                ('end', models.CharField(default='', max_length=10)),
                ('text', models.CharField(default='', max_length=100)),
                ('user', models.CharField(default='', max_length=100)),
                ('user_group', models.CharField(default='0', max_length=3)),
                ('txt', models.CharField(default='', max_length=100)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Txt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(default='0', max_length=3)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=1000)),
            ],
        ),
    ]
