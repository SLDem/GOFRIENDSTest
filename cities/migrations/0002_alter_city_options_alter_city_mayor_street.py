# Generated by Django 4.1.7 on 2023-03-08 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Citie'},
        ),
        migrations.AlterField(
            model_name='city',
            name='mayor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cities.mayor'),
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cities.city')),
            ],
        ),
    ]
