# Generated by Django 4.1.2 on 2022-12-02 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='musteri',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]