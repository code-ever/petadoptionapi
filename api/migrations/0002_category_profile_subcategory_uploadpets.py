# Generated by Django 5.1.1 on 2024-09-25 17:01

import api.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=api.models.Subcategory.category_upload)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
            ],
        ),
        migrations.CreateModel(
            name='Uploadpets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family', models.CharField(blank=True, max_length=200, null=True)),
                ('petname', models.CharField(blank=True, max_length=200, null=True)),
                ('breed', models.CharField(blank=True, max_length=300, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('sex', models.CharField(blank=True, max_length=20, null=True)),
                ('adoption_fee', models.CharField(blank=True, max_length=200, null=True)),
                ('species', models.CharField(blank=True, max_length=300, null=True)),
                ('sRescueID', models.CharField(blank=True, max_length=300, null=True)),
                ('currentSize', models.CharField(blank=True, max_length=300, null=True)),
                ('fenceRequired', models.CharField(blank=True, max_length=300, null=True)),
                ('housetrained', models.CharField(blank=True, max_length=300, null=True)),
                ('obedienceTraining', models.CharField(blank=True, max_length=300, null=True)),
                ('exerciseNeeds', models.CharField(blank=True, max_length=300, null=True)),
                ('ownerExperience', models.CharField(blank=True, max_length=300, null=True)),
                ('reaction_to_New_People', models.CharField(blank=True, max_length=300, null=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to=api.models.Uploadpets.Image_upload)),
                ('postleble', models.CharField(blank=True, choices=[('family', 'family'), ('apatmentdog', 'apatmentdog')], max_length=200, null=True)),
                ('sluge', models.SlugField(blank=True, default=None, max_length=255, null=True)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.profile')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subcategory')),
            ],
        ),
    ]