# Generated by Django 4.0.3 on 2022-03-29 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_user_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rol',
            field=models.CharField(blank=True, max_length=70, verbose_name='Rol'),
        ),
    ]
