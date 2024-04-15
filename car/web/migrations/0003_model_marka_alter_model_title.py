# Generated by Django 5.0.4 on 2024-04-14 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_model_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='marka',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='marka', to='web.marka'),
        ),
        migrations.AlterField(
            model_name='model',
            name='title',
            field=models.CharField(max_length=32),
        ),
    ]
