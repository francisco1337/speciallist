# Generated by Django 4.0.3 on 2022-04-02 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_country_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('town', models.CharField(max_length=100, null=True, verbose_name='Ciudad')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.country', verbose_name='Pais')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.state', verbose_name='Estado')),
            ],
        ),
    ]
