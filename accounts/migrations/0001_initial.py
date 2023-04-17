# Generated by Django 4.1.4 on 2022-12-30 07:43

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
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('dob', models.DateField()),
                ('p1', models.CharField(max_length=100)),
                ('p2', models.CharField(max_length=100)),
                ('secques', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'account_user',
            },
        ),
    ]
