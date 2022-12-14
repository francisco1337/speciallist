# Generated by Django 4.0.3 on 2022-04-02 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_town'),
        ('specialist', '0007_clinic_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='postal_code',
            field=models.IntegerField(default=None, null=True, verbose_name='Codigo postal'),
        ),
        migrations.AddField(
            model_name='clinic',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.state', verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='clinic',
            name='town',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.town', verbose_name='Ciudad/Municipio'),
        ),
    ]
