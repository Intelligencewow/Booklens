# Generated by Django 5.0.3 on 2024-04-03 02:53

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
                ('title', models.CharField(max_length=65)),
                ('author', models.CharField(blank=True, max_length=65, null=True)),
                ('publisher', models.CharField(blank=True, max_length=65, null=True)),
                ('publication_year', models.IntegerField(blank=True, null=True)),
                ('genre', models.CharField(blank=True, max_length=65, null=True)),
                ('cover_image_path', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
