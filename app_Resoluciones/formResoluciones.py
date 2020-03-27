from django import forms

from .models import Resoluciones


class FormResoluciones(forms.ModelForm):
    class Meta:
        model = Resoluciones
        fields = ['no_expediente', 'fecha_resolucion', 'puntos_resolucion', 'sentido_resolucion', 'multa', 'medioImpugnacion']
        labels = {
            'class': 'bm-label-floating',
            'no_expediente': '',
            'fecha_resolucion': '',
            'puntos_resolucion': '',
            'sentido_resolucion': '',
            'multa': '',
            'medioImpugnacion': ''
        }

        widgets = {
            'no_expediente': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Numero de expediente'
                }
            ),
            'fecha_resolucion': forms.TextInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'placeholder': 'Fecha de resolucion'
                }
            ),
            'puntos_resolucion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Puntos de la Resolución'
                }
            ),
            'sentido_resolucion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Sentido de la Resolución'
                }
            ),
            'multa': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'medioImpugnacion': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

        }
