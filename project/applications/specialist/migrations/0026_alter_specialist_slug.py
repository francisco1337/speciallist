# Generated by Django 4.0.3 on 2022-04-16 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialist', '0025_alter_specialist_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialist',
            name='slug',
            field=models.SlugField(blank=True, max_length=300, null=True),
        ),
    ]
