# Generated by Django 3.2.4 on 2021-07-18 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20210705_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('fullname', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('address', models.TextField()),
                ('gender', models.BooleanField()),
            ],
            options={
                'db_table': 'MyUser',
            },
        ),
    ]
