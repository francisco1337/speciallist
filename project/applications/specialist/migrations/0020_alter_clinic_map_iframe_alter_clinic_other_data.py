# Generated by Django 4.0.3 on 2022-04-13 16:37

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialist', '0019_clinic_description_clinic_other_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='map_iframe',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True, verbose_name='Google map'),
        ),
        migrations.AlterField(
            model_name='clinic',
            name='other_Data',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Otros datos'),
        ),
    ]