# Generated by Django 3.1.5 on 2021-04-13 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0004_pagoslistado'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pagoslistado',
            options={'ordering': ['-created'], 'verbose_name': 'Pagos que puede realizar un usuario'},
        ),
    ]
