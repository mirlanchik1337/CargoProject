# Generated by Django 4.2.6 on 2023-10-21 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackcode',
            name='date',
            field=models.DateField(verbose_name='Время'),
        ),
    ]
