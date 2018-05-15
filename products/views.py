# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseBadRequest, HttpRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.core import serializers
import re
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View



from .forms import ProductForm
from .models import Server

class ServerList(ListView):
    
    template_name = 'products/server_list.html'
    
    def get(self, request):
        '''
        metodo get 
        '''
        query = request.GET.get("q")
        sort = request.GET.get("sort", 'name')
        object_list = None
        if query:
            object_list = Server.objects.filter(
                Q(name__icontains=query) |
                Q(client__name__icontains=query) |
                Q(tipe__tipe__icontains=query) |
                Q(interface__name_interface__icontains=query) |
                Q(virtual__virtual__icontains=query)|
                Q(platform__name_platform__icontains=query)|
                Q(system_operative__system_operative__icontains=query)|
                Q(model__icontains=query)|
                Q(service__service__icontains=query)|
                Q(city__city__icontains=query)|
                Q(seat__seat__icontains=query) |
                Q(rack__rack__icontains=query) 
                
            )
        else:
            object_list = Server.objects.all().order_by(sort)
        page =request.GET.get("page")
        output = {
            'object_list': object_list
        }
        return render(request, self.template_name, output)

# vista para crear un nuevo servidor
@login_required()
def new_product(request):
    if request.method == 'POST':
         form = ProductForm(request.POST, request.FILES)
         if form.is_valid():
             product = form.save()
             product.save()
             return HttpResponseRedirect('/')
    else:
        form = ProductForm()  

    template = loader.get_template('new_server.html')
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))


# vista de login y logout
def auth_login(request):
    if request.method == 'POST':
        action = request.POST.get('action', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if action == 'signup':
            user = User.objects.create_user(username=username,
                                            password=password)
            user.save()
        elif action == 'login':
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return HttpResponseRedirect('/')
            else :
                output = {
                    'mensagge' : 'Usuario o contraseña incorrectos',
                }
                return render(request,'login/login.html', output)    
            
    context = {}
    return render(request, 'login/login.html', context)



# vista generica para eliminar un servidor
class ServerDeleteView(DeleteView):
	"""Esta vista nos permitira eliminar un Servidor existente"""
	model = Server
	success_url = reverse_lazy('products:index')


class ServerEditView(View):
    '''
    Clase para editar los servidores
    '''
    template_name = 'edit_server.html'
    
    def get(self, request, *args, **kwargs):
        '''
        Método get
        '''
        asearch = Server.objects.filter(id=kwargs['id']).first()
        form = ProductForm(instance=asearch)

        output = {
            'form': form
        }
        return render(request, self.template_name, output)


    def post(self, request, *args, **kwargs):
        '''
        Método post
        '''
        asearch = Server.objects.filter(id=kwargs['id']).first()
        form = ProductForm(request.POST, instance=asearch)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')    

        output = {
            'form': form,
            'messages': "Revise los campos correctamente.",
        }
        
        return render(request, self.template_name, output)   
