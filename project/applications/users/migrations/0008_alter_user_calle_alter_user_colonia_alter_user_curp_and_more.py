# Generated by Django 4.0.3 on 2022-03-29 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_calle_alter_user_colonia_alter_user_curp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='calle',
            field=models.CharField(max_length=70, verbose_name='Calle'),
        ),
        migrations.AlterField(
            model_name='user',
            name='colonia',
            field=models.CharField(max_length=70, verbose_name='Colonia'),
        ),
        migrations.AlterField(
            model_name='user',
            name='curp',
            field=models.CharField(max_length=200, verbose_name='CURP'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=150, unique=True, verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='estado',
            field=models.CharField(max_length=70, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='user',
            name='estadoCivil',
            field=models.CharField(max_length=70, verbose_name='Estado Civil'),
        ),
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.CharField(max_length=150, verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='user',
            name='municipio',
            field=models.CharField(max_length=70, verbose_name='Municipio'),
        ),
        migrations.AlterField(
            model_name='user',
            name='numero',
            field=models.CharField(max_length=70, verbose_name='Numero'),
        ),
        migrations.AlterField(
            model_name='user',
            name='rfc',
            field=models.CharField(max_length=70, verbose_name='RFc'),
        ),
    ]
