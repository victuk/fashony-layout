# Generated by Django 3.1.7 on 2021-03-07 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=455)),
                ('message', models.TextField(default='', max_length=455)),
            ],
        ),
        migrations.CreateModel(
            name='contestant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('picture', models.ImageField(upload_to='images/')),
                ('contestantsCode', models.CharField(default='', max_length=455)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Unselected', max_length=10)),
                ('description', models.TextField(default='', max_length=455)),
            ],
        ),
        migrations.CreateModel(
            name='youtubelink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('link', models.TextField(default='', max_length=455)),
            ],
        ),
    ]
