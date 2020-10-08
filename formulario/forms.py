from django import forms
from django.conf import settings
from django_select2 import forms as s2forms

from .models import Mapeamento


class PostCityForm(forms.ModelForm):
    data_inicial = forms.DateField(label='Qual a data do arquivo mais antigo disponível online?',
                                   input_formats=settings.DATE_INPUT_FORMATS,
                                   widget=forms.DateInput(attrs={'placeholder':'DD/MM/AAAA'}),
                                   required=False)

    class Meta:
        model = Mapeamento
        fields = ('municipio', 'is_online','data_inicial', 'tipo_arquivo', 'fonte_1', 'fonte_2', 'fonte_3',
                  'fonte_4',)
        widgets = {'municipio': s2forms.Select2Widget}
        labels = {
            'municipio': 'Selecione o município',
            'fonte_1': 'Informe uma fonte de publicação de arquivos',
            'fonte_2': 'Informe uma fonte de publicação de arquivos',
            'fonte_3': 'Informe uma fonte de publicação de arquivos',
            'fonte_4': 'Informe uma fonte de publicação de arquivos',
            'is_online': 'Existe uma fonte de publicação disponível online?',
            'tipo_arquivo': 'Qual o formato dos arquivos?',
        }