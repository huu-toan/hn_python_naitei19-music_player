# Generated by Django 3.2.20 on 2023-10-02 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20231001_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='tags',
            field=models.ManyToManyField(through='catalog.SongTag', to='catalog.Tag'),
        ),
    ]