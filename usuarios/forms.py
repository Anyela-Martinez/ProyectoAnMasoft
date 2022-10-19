from dataclasses import field, fields
from django import forms
from usuarios.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields="__all__"