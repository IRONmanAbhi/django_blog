# Generated by Django 5.1.2 on 2024-11-03 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_edited'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='edited',
            field=models.IntegerField(default=0),
        ),
    ]