# Generated by Django 4.0.3 on 2022-03-31 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialist', '0003_alter_schedule_domingo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='domingo',
            field=models.JSONField(verbose_name='Domingo'),
        ),
    ]
