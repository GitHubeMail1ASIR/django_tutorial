# Generated by Django 4.1.5 on 2023-01-24 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='Cantidad',
            field=models.IntegerField(default=0),
        ),
    ]
