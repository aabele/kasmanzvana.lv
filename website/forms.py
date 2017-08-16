"""
Application forms
"""

from django import forms

from website.models import Message


class ContactForm(forms.ModelForm):
    """
    Login form with email as username
    """
    class Meta(object):
        model = Message
        fields = ['email', 'body']
        widgets = {
            'email': forms.TextInput(attrs={
                'placeholder': 'Jūsu epasts',
                'class': 'form-control form-control-lg'
            }),
            'body': forms.Textarea(attrs={
                'placeholder': 'Jautājums',
                'class': 'form-control form-control-lg',
                'rows': 4,
            })
        }
