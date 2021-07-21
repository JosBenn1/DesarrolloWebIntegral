# Generated by Django 3.1.5 on 2021-04-20 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0013_auto_20210416_0342'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
            ],
            options={
                'verbose_name': 'estado',
                'verbose_name_plural': 'ESTATUS',
            },
        ),
    ]