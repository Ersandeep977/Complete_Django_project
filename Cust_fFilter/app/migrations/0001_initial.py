# Generated by Django 3.0.5 on 2020-05-03 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RDate', models.DateField()),
                ('MovieName', models.CharField(max_length=30)),
                ('HeroName', models.CharField(max_length=30)),
                ('HeroineName', models.CharField(max_length=30)),
                ('Rating', models.IntegerField()),
            ],
        ),
    ]
