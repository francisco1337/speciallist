# Generated by Django 4.0.3 on 2022-03-29 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_calle_alter_user_colonia_alter_user_curp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rol',
            field=models.CharField(max_length=70, null=True, verbose_name='Rol'),
        ),
    ]
