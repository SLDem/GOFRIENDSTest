# Generated by Django 4.1.7 on 2023-03-08 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_alter_city_options_alter_city_mayor_street'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mayor',
            name='date_of_job_start',
            field=models.DateField(null=True),
        ),
    ]
