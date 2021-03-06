# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-04 18:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255, verbose_name='Ciudad')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('phone', models.IntegerField(unique=True, verbose_name='Telefono')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Correo')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_red', models.IntegerField(verbose_name='Numero de reds')),
                ('name_interface', models.CharField(max_length=255, verbose_name='Nombre interfaz')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Interfaz',
                'verbose_name_plural': 'Interfaces',
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_platform', models.CharField(max_length=255, verbose_name='Nombre de Plataforma')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Plataforma',
                'verbose_name_plural': 'Plataformas',
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat', models.CharField(max_length=255, verbose_name='Sede')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Sede',
                'verbose_name_plural': 'Sedes',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('model', models.CharField(max_length=255, verbose_name='Modelo')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.City', verbose_name='Ciudad')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Client', verbose_name='Ciudad')),
                ('interface', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Interface', verbose_name='Interfaz')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Platform', verbose_name='Plataforma')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Servidor',
                'verbose_name_plural': 'Servidores',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=255, verbose_name='Servicio')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
        migrations.CreateModel(
            name='SystemOperative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_operative', models.CharField(max_length=255, verbose_name='Sistema Operativo')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Sistema Operativo',
                'verbose_name_plural': 'Sistemas Operativos',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipe', models.CharField(max_length=255, verbose_name='Tipo')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
            },
        ),
        migrations.CreateModel(
            name='Virtual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('virtual', models.CharField(max_length=255, verbose_name='Virtualizacion')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Virtualizacion',
            },
        ),
        migrations.RemoveField(
            model_name='servidor',
            name='Ciudad',
        ),
        migrations.RemoveField(
            model_name='servidor',
            name='Cliente',
        ),
        migrations.RemoveField(
            model_name='servidor',
            name='Interfaz',
        ),
        migrations.RemoveField(
            model_name='servidor',
            name='Plataforma',
        ),
        migrations.RemoveField(
            model_name='servidor',
            name='Rack',
        ),
        migrations.RemoveField(
            model_name='servidor',
            name='Sede',
        ),
        migrations.RemoveField(
            model_name='servidor',
            name='Servicios',
        ),
        migrations.RemoveField(
            model_name='servidor',
            name='Sistema_operativo',
        ),
        migrations.RemoveField(
            model_name='servidor',
            name='Tipo',
        ),
        migrations.AlterModelOptions(
            name='rack',
            options={'ordering': ('id',), 'verbose_name': 'Rack', 'verbose_name_plural': 'Racks'},
        ),
        migrations.AlterField(
            model_name='rack',
            name='rack',
            field=models.CharField(max_length=255, verbose_name='Rack'),
        ),
        migrations.DeleteModel(
            name='Ciudad',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Interfaz',
        ),
        migrations.DeleteModel(
            name='Plataforma',
        ),
        migrations.DeleteModel(
            name='Sede',
        ),
        migrations.DeleteModel(
            name='Servicio',
        ),
        migrations.DeleteModel(
            name='Servidor',
        ),
        migrations.DeleteModel(
            name='Sistema',
        ),
        migrations.DeleteModel(
            name='Tipo',
        ),
        migrations.AddField(
            model_name='server',
            name='rack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Rack', verbose_name='Rack'),
        ),
        migrations.AddField(
            model_name='server',
            name='seat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Seat', verbose_name='Sede'),
        ),
        migrations.AddField(
            model_name='server',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Service', verbose_name='Servicio'),
        ),
        migrations.AddField(
            model_name='server',
            name='system_operative',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.SystemOperative', verbose_name='Sistema Operativo'),
        ),
        migrations.AddField(
            model_name='server',
            name='tipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Type', verbose_name='Tipo'),
        ),
        migrations.AddField(
            model_name='server',
            name='virtual',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Virtual', verbose_name='Virtualizacion'),
        ),
    ]
