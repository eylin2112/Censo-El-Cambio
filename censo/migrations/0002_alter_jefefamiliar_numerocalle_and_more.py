# Generated by Django 4.2.6 on 2023-11-22 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('censo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jefefamiliar',
            name='numeroCalle',
            field=models.PositiveIntegerField(max_length=4, verbose_name='Numero de calle'),
        ),
        migrations.AlterField(
            model_name='jefefamiliar',
            name='numeroCasa',
            field=models.PositiveIntegerField(max_length=3, verbose_name='Numero de Casa'),
        ),
    ]