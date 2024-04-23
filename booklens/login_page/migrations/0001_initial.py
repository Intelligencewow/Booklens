# Generated by Django 5.0.3 on 2024-04-10 00:59

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('author', models.CharField(blank=True, max_length=65, null=True)),
                ('publisher', models.CharField(blank=True, max_length=65, null=True)),
                ('publication_year', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(9999)])),
                ('genre', models.CharField(blank=True, max_length=65, null=True)),
                ('cover_image_path', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('content', models.CharField(max_length=200)),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('BookId', models.ForeignKey(db_column='BookId', on_delete=django.db.models.deletion.CASCADE, to='login_page.book')),
                ('UserId', models.ForeignKey(db_column='UserId', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'review',
            },
        ),
    ]
