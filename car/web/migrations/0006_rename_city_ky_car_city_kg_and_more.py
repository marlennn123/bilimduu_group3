# Generated by Django 5.0.4 on 2024-04-16 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_car_city_en_car_city_ky_car_city_ru_car_color_en_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='city_ky',
            new_name='city_kg',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='color_ky',
            new_name='color_kg',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='country_ky',
            new_name='country_kg',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='description_ky',
            new_name='description_kg',
        ),
        migrations.RenameField(
            model_name='carbet',
            old_name='number_ky',
            new_name='number_kg',
        ),
        migrations.RenameField(
            model_name='carbet',
            old_name='total_number_ky',
            new_name='total_number_kg',
        ),
    ]