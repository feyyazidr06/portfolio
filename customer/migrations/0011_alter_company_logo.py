# Generated by Django 4.1.2 on 2022-12-04 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_alter_company_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='customer/logo'),
        ),
    ]
