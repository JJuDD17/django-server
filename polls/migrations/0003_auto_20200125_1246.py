# Generated by Django 3.0.2 on 2020-01-25 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='image'),
        ),
    ]
