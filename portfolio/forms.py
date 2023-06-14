from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth import get_user_model

class PostForm(ModelForm):
    autor = forms.ModelChoiceField(queryset=Pessoa.objects.all())

    class Meta:
        model = Post
        fields = ['titulo', 'autor', 'descricao', 'link','imagem']

    # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'autor'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'titulo'}),
            'link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'link'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descricao'}),
        }


    # texto a exibir junto à janela de inserção
        labels = {
            'autor': 'Autor',
            'titulo': 'Título',
            'link': 'Link',
            'descricao': 'Descrição',
        }

#CADEIRAS FORM 
class CadeiraForm(forms.ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'

#CADEIRAS FORM 
class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

