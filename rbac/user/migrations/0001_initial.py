# Generated by Django 3.1.4 on 2021-01-01 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=20)),
                ('is_delete', models.IntegerField(choices=[(0, '否'), (1, '是')], default=0)),
                ('is_active', models.IntegerField(choices=[(0, '否'), (1, '是')], default=1)),
                ('is_superuser', models.IntegerField(choices=[(0, '否'), (1, '是')], default=0)),
                ('is_staff', models.IntegerField(choices=[(0, '否'), (1, '是')], default=1)),
                ('utm', models.BigIntegerField()),
                ('ctm', models.BigIntegerField()),
            ],
        ),
    ]
