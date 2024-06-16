from django import forms
from berita.models import Artikel
from django import forms

class ArtikelForm(forms.ModelForm):

    class Meta:
        model = Artikel
        fields = ('judul','isi','Kategori','thumbnail')
        widgets = {
        
            "judul" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                }),
            "isi" : forms.Textarea(
                attrs={
                    'class': 'form-control',
                }),
            "kategori" : forms.Select(
                attrs={
                    'class': 'form-control',
                }),
    }