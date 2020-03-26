from django import forms

from .models import MediosImpugnacion


class FormMediosImpugnacion(forms.ModelForm):
    class Meta:
        model = MediosImpugnacion
        fields = ['no_expediente', 'fecha_emplazamiento', 'tipo_medioImpugnacion', 'efecto_medioImpugnacion', 'comentarios', 'medidas_apremio']
        labels ={
            'class': 'bm-label-floating',
            'no_expediente': '',
            'fecha_emplazamiento': '',
            'tipo_medioImpugnacion': '',
            'efecto_medioImpugnacion': '',
            'comentarios': '',
            'medidas_apremio': ''
        }

        widgets = {
            'no_expediente': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Numero de expediente'
                }
            ),
            'fecha_emplazamiento': forms.TextInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'placeholder': 'Fecha de Emplazamiento',
                }
            ),
            'tipo_medioImpugnacion': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Tipo de Medio de Impugnación'
                }
            ),
            'efecto_medioImpugnacion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Efecto del Medio de Impugnación'
                }
            ),
            'comentarios': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Comentarios'
                }
            ),
            'medidas_apremio': forms.Select(
                attrs={
                   'class': 'form-control'
                }
            ),
        }
