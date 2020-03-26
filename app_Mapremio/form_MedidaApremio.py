from django import forms
from .models import MedidasdeApremio


class MedidasdeApremioForm(forms.ModelForm):
    class Meta:
        model = MedidasdeApremio
        fields = ['no_expediente', 'motivos', 'SujetoObligado', 'nombreCortoSo', 'cantidad', 'tipoMedida',
                  'fechaEmision']
        labels = {'class': 'bm-label-floating',
                  'no_expediente': '',
                  'motivos': '',
                  'SujetoObligado': '',
                  'nombreCortoSo': '',
                  'cantidad': '',
                  'tipoMedida': '',
                  'fechaEmision': ''
                  }
        widgets = {
            'no_expediente': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Numero de expediente'
                }
            ),
            'motivos': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Motivos'

                }
            ),
            'SujetoObligado': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del Sujeto Obligado'

                }
            ),
            'nombreCortoSo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre corto del Sujeto Obligado'

                }
            ),
            'cantidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '$ Cantidad'

                }
            ),
            'tipoMedida': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Tipo de medida de apremio'

                }
            ),
            'fechaEmision': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Fecha de emisión'

                }
            ),
            # 'usuario': forms.Select(
            #     attrs={
            #         'class': 'form-control',
            #         'placeholder': 'Usuario'
            #
            #     }
            # )
        }
