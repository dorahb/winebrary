# Generated by Django 4.1.1 on 2022-12-14 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_wishlist_complete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='complete',
        ),
    ]
