# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Server, Client, Interface, Type, Platform, SystemOperative, Service, City, Seat, Rack, Virtual
from django.contrib import admin

@admin.register(Rack)
class AdminRack(admin.ModelAdmin):
    list_display = ('rack',)
    list_filter = ('rack',)

@admin.register(Seat)
class AdminSeat(admin.ModelAdmin):
    list_display = ('seat',)
    list_filter = ('seat',)

@admin.register(City)
class AdminServicio(admin.ModelAdmin):
    list_display = ('city',)
    list_filter = ('city',)


@admin.register(Service)
class AdminService(admin.ModelAdmin):
    list_display = ('service',)
    list_filter = ('service',)

@admin.register(SystemOperative)
class AdminSystemOperative(admin.ModelAdmin):
    list_display = ('system_operative',)
    list_filter = ('system_operative',)

@admin.register(Platform)
class AdminPlatform(admin.ModelAdmin):
    list_display = ('name_platform',)
    list_filter = ('name_platform',)

@admin.register(Type)
class AdminType(admin.ModelAdmin):
    list_display = ('tipe',)
    list_filter = ('tipe',)



@admin.register(Interface)
class AdminInterface(admin.ModelAdmin):
    list_display = ('name_interface', 'number_red')
    list_filter = ('name_interface',)
 
@admin.register(Client)
class AdminClient(admin.ModelAdmin):
     list_display = ('name', 'phone', 'email')
     list_filter = ('name',)

@admin.register(Virtual)
class AdminVirtual(admin.ModelAdmin):
    list_display = ('virtual',)
    list_filter = ('virtual',)

@admin.register(Server)
class AdminServer(admin.ModelAdmin):
    list_display = ('name', 'tipe',  'interface',  'virtual', 'platform', 'model', 'service', 'city', 'seat', 'rack')
    list_filter = ('name', 'tipe')