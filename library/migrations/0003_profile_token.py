# Generated by Django 4.1.1 on 2022-12-27 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_book_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='token',
            field=models.IntegerField(default=0),
        ),
    ]
