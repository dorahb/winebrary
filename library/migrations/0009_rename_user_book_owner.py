# Generated by Django 4.1.1 on 2022-11-16 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_alter_book_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='user',
            new_name='owner',
        ),
    ]