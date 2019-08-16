# Generated by Django 2.2.4 on 2019-08-16 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, verbose_name='昵称')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('email', models.CharField(max_length=50, unique=True, verbose_name='邮箱')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='手机号')),
                ('icon', models.CharField(blank=True, max_length=255, null=True, verbose_name='头像')),
                ('intro', models.TextField(blank=True, null=True, verbose_name='简介')),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '用户表(my)',
                'verbose_name_plural': '用户表(my)',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('myid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='myid', to='index.User')),
                ('yid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='yid', to='index.User')),
            ],
            options={
                'verbose_name': '关注',
                'verbose_name_plural': '关注',
                'db_table': 'follow',
            },
        ),
    ]
