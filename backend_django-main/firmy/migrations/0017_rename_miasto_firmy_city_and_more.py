# Generated by Django 4.0.5 on 2022-06-09 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firmy', '0016_rename_zdjecia_firmy_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='firmy',
            old_name='miasto',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='firmy',
            old_name='opis',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='firmy',
            old_name='telefon',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='firmy',
            old_name='strona_www',
            new_name='website',
        ),
    ]
