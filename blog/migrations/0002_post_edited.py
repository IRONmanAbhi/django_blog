# Generated by Django 5.1.2 on 2024-11-03 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='edited',
            field=models.IntegerField(default=0),
        ),
    ]
