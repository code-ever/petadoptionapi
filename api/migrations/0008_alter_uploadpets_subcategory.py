# Generated by Django 5.1.1 on 2024-09-26 19:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_uploadpets_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadpets',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.subcategory'),
        ),
    ]