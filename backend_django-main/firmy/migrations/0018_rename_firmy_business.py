# Generated by Django 4.0.5 on 2022-06-09 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firmy', '0017_rename_miasto_firmy_city_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Firmy',
            new_name='Business',
        ),
    ]
