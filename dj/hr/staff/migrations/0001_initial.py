# Generated by Django 4.2.1 on 2023-05-17 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hrdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='User Name')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
            ],
        ),
    ]
