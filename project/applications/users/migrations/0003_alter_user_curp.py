# Generated by Django 4.0.3 on 2022-03-27 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_lastnames_alter_user_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='curp',
            field=models.CharField(max_length=200, verbose_name='CURP'),
        ),
    ]
