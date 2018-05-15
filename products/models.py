# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Clientes
class Client(models.Model):
    name = models.CharField('Nombre', max_length=255)
    phone = models.IntegerField('Telefono', unique=True)
    email = models.EmailField('Correo', max_length=255, unique=True)
    
    def __str__(self):
        return '%s' % self.name

    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Clientes'
    	verbose_name = 'Cliente'

# Tipo
class Type(models.Model):
    tipe = models.CharField('Tipo', max_length=255)

    def __str__(self):
        return '%s' % self.tipe
    
    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Tipos'
        verbose_name = 'Tipo'

#  Interfaz
class Interface(models.Model):
    number_red = models.IntegerField('Numero de reds', unique=False)
    name_interface = models.CharField('Nombre interfaz', max_length=255)

    def __str__(self):
        return '%s' % self.name_interface
    
    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Interfaces'
        verbose_name = 'Interfaz'

# Plataforma
class Platform(models.Model):
    name_platform = models.CharField('Nombre de Plataforma', max_length=255)

    def __str__(self):
        return '%s' % self.name_platform
    
    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Plataformas'
        verbose_name = 'Plataforma'
        

# Servicio
class Service(models.Model):
    service = models.CharField('Servicio', max_length=255)

    def __str__(self):
        return '%s' % self.service
    
    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Servicios'
        verbose_name = 'Servicio'

# Ciudad
class City(models.Model):
    city = models.CharField('Ciudad', max_length=255)

    def __str__(self):
        return '%s' % self.city
    
    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Ciudades'
        verbose_name = 'Ciudad'

# Sede
class Seat(models.Model):
    seat = models.CharField('Sede', max_length=255)

    def __str__(self):
        return '%s' % self.seat

    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Sedes'
        verbose_name = 'Sede'
# Rack
class Rack(models.Model):
    rack = models.CharField('Rack', max_length=255)

    def __str__(self):
        return '%s' % self.rack

    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Racks'
        verbose_name = 'Rack'

# Virtualizacion
class Virtual(models.Model):
    virtual = models.CharField('Virtualizacion', max_length=255,)

    def __str__(self):
        return '%s' % self.virtual
    class Meta:
        ordering = ('id',)
        verbose_name = 'Virtualizacion'

# Sistema operativo
class SystemOperative(models.Model):
    system_operative = models.CharField('Sistema Operativo', max_length=255)

    def __str__(self):
        return '%s' % self.system_operative

    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Sistemas Operativos'
        verbose_name = 'Sistema Operativo'

# Servidor
class Server(models.Model):
    name = models.CharField('Nombre',max_length=255)
    client = models.ForeignKey(Client, verbose_name= 'Cliente', on_delete=models.CASCADE)
    tipe = models.ForeignKey(Type,verbose_name='Tipo', on_delete=models.CASCADE)
    interface = models.ForeignKey(Interface, verbose_name='Interfaz',  on_delete=models.CASCADE)
    virtual = models.ForeignKey(Virtual, verbose_name='Virtualizacion', on_delete=models.CASCADE)  # un checkd
    platform = models.ForeignKey(Platform, verbose_name='Plataforma', on_delete=models.CASCADE)
    system_operative = models.ForeignKey(SystemOperative, verbose_name='Sistema Operativo',  on_delete=models.CASCADE)
    model = models.CharField('Modelo', max_length=255)
    service = models.ForeignKey(Service, verbose_name='Servicio', on_delete=models.CASCADE)
    city = models.ForeignKey(City, verbose_name='Ciudad', on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, verbose_name='Sede', on_delete=models.CASCADE)
    rack = models.ForeignKey(Rack, verbose_name='Rack',  on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.name
    
    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Servidores'
        verbose_name = 'Servidor'
