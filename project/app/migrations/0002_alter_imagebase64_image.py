# Generated by Django 3.2.20 on 2023-08-22 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagebase64',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]