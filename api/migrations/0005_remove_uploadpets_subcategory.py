# Generated by Django 5.1.1 on 2024-09-26 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_uploadpets_category_alter_subcategory_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadpets',
            name='subcategory',
        ),
    ]