# Generated by Django 3.2.4 on 2021-07-05 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_baibao_publication'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporter',
            name='address',
            field=models.TextField(default='Hồ Chí Minh', verbose_name='Địa chỉ'),
        ),
        migrations.AlterField(
            model_name='reporter',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Địa chỉ email'),
        ),
        migrations.AlterField(
            model_name='reporter',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='Tên'),
        ),
        migrations.AlterField(
            model_name='reporter',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Họ'),
        ),
    ]
