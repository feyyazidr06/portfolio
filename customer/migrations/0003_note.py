# Generated by Django 4.1.2 on 2022-12-03 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_musteri_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=64, null=True)),
                ('content', models.CharField(blank=True, max_length=512, null=True)),
            ],
        ),
    ]
