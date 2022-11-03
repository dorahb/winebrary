# Generated by Django 4.1.1 on 2022-11-03 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('synopsis', models.CharField(max_length=1000)),
                ('pub_date', models.DateTimeField(verbose_name='date posted')),
            ],
        ),
    ]
