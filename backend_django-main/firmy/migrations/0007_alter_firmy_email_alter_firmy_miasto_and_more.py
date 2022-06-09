# Generated by Django 4.0.4 on 2022-06-07 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firmy', '0006_firmy_miasto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firmy',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='firmy',
            name='miasto',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='firmy',
            name='strona_www',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='firmy',
            name='telefon',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='firmy',
            name='zdjecia',
            field=models.ImageField(default='default.png', upload_to='upload_avatar/'),
        ),
    ]