from django import forms
from .models import Cita

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
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'motivo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese el motivo de la cita', 'rows': 3}),
        }
