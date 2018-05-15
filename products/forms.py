from django import forms
from .models import Server, Client

class ProductForm(forms.ModelForm):

    class Meta:
        model = Server
         #fields = '__all__'     
        fields = ['name', 'client', 'tipe', 'interface', 'virtual', 'platform', 'system_operative', 'model', 'service', 'city', 'seat', 'rack'  ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control '}),
            'client': forms.Select(attrs={'class': 'form-control '}),
            'tipe': forms.Select(attrs={'class': 'form-control '}),
            'interface': forms.Select(attrs={'class': 'form-control '}),
            'virtual': forms.Select(attrs={'class': 'form-control '}),
            'platform': forms.Select(attrs={'class': 'form-control '}),
            'system_operative': forms.Select(attrs={'class': 'form-control '}),
            'model': forms.TextInput(attrs={'class': 'form-control '}),
            'service': forms.Select(attrs={'class': 'form-control '}),
            'city': forms.Select(attrs={'class': 'form-control '}),
            'seat': forms.Select(attrs={'class': 'form-control '}),
            'rack': forms.Select(attrs={'class': 'form-control '}),

        }

        