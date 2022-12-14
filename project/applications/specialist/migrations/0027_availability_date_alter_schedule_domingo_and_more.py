# Generated by Django 4.0.3 on 2022-04-17 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialist', '0026_alter_specialist_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='date',
            field=models.DateField(default=None, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='domingo',
            field=models.JSONField(blank=True, null=True, verbose_name='Domingo'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='jueves',
            field=models.JSONField(blank=True, null=True, verbose_name='Jueves'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='lunes',
            field=models.JSONField(blank=True, null=True, verbose_name='Lunes'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='martes',
            field=models.JSONField(blank=True, null=True, verbose_name='Martes'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='miercoles',
            field=models.JSONField(blank=True, null=True, verbose_name='Miercoles'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='sabado',
            field=models.JSONField(blank=True, null=True, verbose_name='Sabado'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='viernes',
            field=models.JSONField(blank=True, null=True, verbose_name='Viernes'),
        ),
    ]
