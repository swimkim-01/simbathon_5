# Generated by Django 3.2 on 2021-06-23 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_id', models.IntegerField()),
                ('writer', models.CharField(max_length=100)),
                ('room', models.CharField(max_length=100)),
                ('res_time', models.DateTimeField()),
            ],
        ),
    ]
