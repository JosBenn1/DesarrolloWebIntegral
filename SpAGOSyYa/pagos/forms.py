from django import forms
from .models import PagoSolicitado
import uuid

class RegForm(forms.ModelForm):
        class Meta:
            model = PagoSolicitado
            fields = ['image']
     
        image = forms.ImageField(widget=forms.FileInput(attrs={'type':'file'}))

class PayForm(forms.ModelForm):
        class Meta:
            model = PagoSolicitado
            fields = ['cuatrimestre','motivo', 'descripcion','beca','cantidad']
        
            
        
        cuatrimestre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        motivo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        beca = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        cantidad = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
