from django import forms
from .models import Cita
from django.core.exceptions import ValidationError
import re
from datetime import date

# Validador personalizado para permitir solo letras y espacios en el nombre
def validar_nombre(value):
    if not re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", value):
        raise ValidationError('El nombre solo puede contener letras y espacios.')

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['nombre', 'rut', 'fecha', 'hora', 'motivo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del cliente'}),
            'rut': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el RUT',
                'maxlength': '12',
                'oninput': 'formatRut(this)'
            }),
            'fecha': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'min': date.today().strftime('%Y-%m-%d')  # Asegura que la fecha sea desde hoy
            }),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'motivo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese el motivo de la cita', 'rows': 3}),
        }

    # Se agrega el validador al campo 'nombre'
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        validar_nombre(nombre)  # Llama al validador
        return nombre