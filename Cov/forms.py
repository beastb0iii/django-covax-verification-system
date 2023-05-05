from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'contacts', 'address', 'status']
        widgets = {
        'name': forms.TextInput(attrs={'class':'form-control', 'autocomplete': 'off'}),
        'contacts': forms.TextInput(attrs={'class':'form-control', 'autocomplete': 'off'}),
        'address': forms.TextInput(attrs={'class':'form-control', 'autocomplete': 'off'}),
        'status': forms.TextInput(attrs={'class':'form-control', 'autocomplete': 'off'} ),
    }

