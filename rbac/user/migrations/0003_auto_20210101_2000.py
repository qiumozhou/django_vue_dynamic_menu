# Generated by Django 3.1.4 on 2021-01-01 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210101_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ctm',
            field=models.BigIntegerField(verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='utm',
            field=models.BigIntegerField(verbose_name='更新时间'),
        ),
    ]
