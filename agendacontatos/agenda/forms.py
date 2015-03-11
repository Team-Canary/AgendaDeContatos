from django import forms
from models import ItemAgenda

class FormItemAgenda(forms.ModelForm):
    class Meta:
        model = ItemAgenda
        fields = ('nome', 'email', 'telefone1', 'telefone2', 'endereco', 'redeSocial')
