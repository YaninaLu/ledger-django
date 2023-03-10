# Generated by Django 4.1.4 on 2022-12-20 10:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Spending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('amount', models.CharField(max_length=7)),
                ('comment', models.TextField(max_length=400)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ledgerapp.category')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Earning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('amount', models.CharField(max_length=7)),
                ('comment', models.TextField(max_length=400)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ledgerapp.source')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
