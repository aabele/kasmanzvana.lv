from django import forms
from user import models


class EmailForm(forms.ModelForm):

    class Meta(object):
        model = models.User
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Jūsu epasts',
                'class': 'form-control form-control-lg'
            })
        }
