# Generated by Django 3.0.5 on 2020-04-29 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='empDesig',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='emp',
            name='empid',
            field=models.CharField(max_length=20),
        ),
    ]
