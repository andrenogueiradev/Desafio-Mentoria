# Generated by Django 3.2.7 on 2021-09-06 18:04

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
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('status', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=90)),
                ('city', models.CharField(max_length=30)),
                ('managers', models.ManyToManyField(blank=True, related_name='company', to=settings.AUTH_USER_MODEL, verbose_name='managers')),
            ],
            options={
                'verbose_name_plural': 'Company',
            },
        ),
    ]