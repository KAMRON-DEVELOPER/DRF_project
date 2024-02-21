# Generated by Django 4.1 on 2024-02-21 04:06

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('description', models.TextField()),
                ('isbn', models.CharField(max_length=17)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('publish', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]