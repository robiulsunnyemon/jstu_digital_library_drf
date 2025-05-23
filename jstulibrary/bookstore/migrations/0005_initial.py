# Generated by Django 5.2.1 on 2025-05-19 19:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bookstore', '0004_delete_book_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('writer', models.CharField(max_length=255)),
                ('fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('validation', models.IntegerField(help_text='Validation period in days')),
                ('item', models.IntegerField(default=1)),
                ('available', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='bookstore.category')),
            ],
        ),
    ]
