# Generated by Django 5.1.4 on 2024-12-30 04:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('published_date', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginapp.author')),
            ],
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_books', models.ManyToManyField(to='loginapp.book')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='loginapp.author')),
            ],
        ),
    ]
