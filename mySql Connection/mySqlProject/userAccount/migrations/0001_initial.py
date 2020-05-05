# Generated by Django 3.0.5 on 2020-05-02 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('mailid', models.EmailField(max_length=254)),
                ('image', models.FileField(upload_to='images/')),
            ],
        ),
    ]
