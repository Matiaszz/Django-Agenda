from typing import Any
from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone')

    def clean(self) -> dict[str, Any]:
        # cleaned_data = self.cleaned_data
        self.add_error('first_name', ValidationError(
            'Mensagem de erro', code='invalid'
        ))
        self.add_error('first_name', ValidationError(
            'Mensagem de erro 2', code='invalid'
        ))
        return super().clean()
