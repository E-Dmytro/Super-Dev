# Generated by Django 3.1.1 on 2020-09-28 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('surname', models.CharField(blank=True, max_length=20)),
                ('patronymic', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
