# Generated by Django 4.1.1 on 2022-11-16 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_rename_user_book_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='owner',
            new_name='user',
        ),
    ]