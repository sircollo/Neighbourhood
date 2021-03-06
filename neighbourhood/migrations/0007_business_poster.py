# Generated by Django 4.0.4 on 2022-06-20 10:51

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0006_alter_business_neighbourhood_alter_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='poster',
            field=cloudinary.models.CloudinaryField(default='image.jpg', max_length=255, null=True, verbose_name='Poster'),
        ),
    ]
