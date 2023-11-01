from django import forms
from .models import *


class AddPostForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select category"

    class Meta:
        model = Women
        fields = [
            'title', 'slug', 'content', 'photo', 'is_published', 'category',
            'films'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'slug': forms.TextInput(attrs={'class': 'form-input'}),
        }


class AddFilmData(forms.ModelForm):
    class Meta:
        model = Films
        fields = ['films', ]
        widgets = {
            'films': forms.TextInput(attrs={'class': 'form-input'}),
        }
