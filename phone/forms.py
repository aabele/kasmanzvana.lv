"""
Application forms
"""
from django import forms

from phone import models


class CommentForm(forms.ModelForm):
    """
    Create commentary in a phone page
    """
    phone = forms.CharField()

    def clean_phone(self):
        data = self.cleaned_data.get('phone')
        obj, _ = models.Phone.objects.get_or_create(phone=data)
        return obj

    class Meta(object):
        """
        Modelform meta options
        """
        model = models.Comment
        fields = ['phone', 'body']
        widgets = {
            'phone': forms.HiddenInput,
            'body': forms.Textarea,
        }
