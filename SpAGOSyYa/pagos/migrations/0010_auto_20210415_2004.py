# Generated by Django 3.1.5 on 2021-04-16 01:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0009_auto_20210415_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagossolicitado',
            name='refpago',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='Fecha de emision'),
        ),
    ]