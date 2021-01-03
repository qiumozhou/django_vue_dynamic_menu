# Generated by Django 3.1.4 on 2021-01-01 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': '用户表'},
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=20, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.IntegerField(choices=[(0, '否'), (1, '是')], default=1, verbose_name='是否启用'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_delete',
            field=models.IntegerField(choices=[(0, '否'), (1, '是')], default=0, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.IntegerField(choices=[(0, '否'), (1, '是')], default=1, verbose_name='是否员工'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.IntegerField(choices=[(0, '否'), (1, '是')], default=0, verbose_name='是否管理员'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=30, verbose_name='用户名'),
        ),
        migrations.AlterModelTable(
            name='user',
            table='tb_user',
        ),
    ]
