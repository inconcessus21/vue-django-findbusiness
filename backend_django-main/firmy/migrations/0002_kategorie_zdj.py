# Generated by Django 4.0.4 on 2022-05-21 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firmy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kategorie',
            name='zdj',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
