# Generated by Django 4.0.6 on 2022-08-19 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField(max_length=1000)),
                ('short_url', models.URLField(blank=True, max_length=30, null=True)),
            ],
            options={
                'unique_together': {('original_url', 'short_url')},
            },
        ),
    ]
