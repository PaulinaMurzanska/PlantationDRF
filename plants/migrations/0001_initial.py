# Generated by Django 3.1.3 on 2020-12-19 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=150)),
                ('image_url', models.URLField(blank=True, default='')),
                ('slug', models.SlugField(unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=150)),
                ('watering_interval', models.PositiveIntegerField(help_text='in seconds')),
                ('fertilizing_interval', models.PositiveIntegerField(help_text='in seconds')),
                ('required_exposure', models.CharField(choices=[('dark', 'Dark'), ('shade', 'Shade'), ('partsun', 'Part Sun'), ('fullsun', 'Full Sun')], max_length=10, verbose_name='Amount of sun')),
                ('required_humidity', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], max_length=10)),
                ('required_temperature', models.CharField(choices=[('cold', 'Cold'), ('medium', 'Medium'), ('warm', 'Warm')], max_length=10)),
                ('blooming', models.BooleanField(blank=True, default=False, verbose_name='blooming?')),
                ('difficulty', models.PositiveIntegerField(choices=[(1, 'low'), (2, 'medium low'), (3, 'medium'), (4, 'medium high'), (5, 'high')], default=1, verbose_name='Cultivation difficulty level')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='plants.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=150)),
                ('exposure', models.CharField(choices=[('dark', 'Dark'), ('shade', 'Shade'), ('partsun', 'Part Sun'), ('fullsun', 'Full Sun')], max_length=10, verbose_name='Amount of sun')),
                ('humidity', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], max_length=10)),
                ('temperature', models.CharField(choices=[('cold', 'Cold'), ('medium', 'Medium'), ('warm', 'Warm')], max_length=10)),
                ('drafty', models.BooleanField(blank=True, default=False, verbose_name='drafty?')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserPlant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=150)),
                ('image_url', models.URLField(blank=True, default='')),
                ('last_watered', models.DateTimeField(blank=True, null=True, verbose_name='Timestamp of last watering')),
                ('last_fertilized', models.DateTimeField(blank=True, null=True, verbose_name='Timestamp of last fertizing')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='plants.plant', verbose_name='Type of plant')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='plants.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
