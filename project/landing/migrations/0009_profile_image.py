# Generated by Django 4.0.5 on 2023-03-17 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0008_auto_20230317_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profil_foto/'),
        ),
    ]
