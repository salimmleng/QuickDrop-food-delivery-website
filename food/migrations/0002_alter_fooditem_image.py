# Generated by Django 5.0.6 on 2024-09-02 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='image',
            field=models.ImageField(upload_to='food/food_images/'),
        ),
    ]
