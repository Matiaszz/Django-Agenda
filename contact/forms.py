from typing import Any
from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone',
                  'email', 'description', 'category', 'picture')
        widgets = {
            field: forms.TextInput(attrs={
                'placeholder': f'Type your {field.replace("_", " ")}'})
            for field in fields if field not in [
                'description',
                'category',
                'email',
                'picture'
            ]
        }
        widgets['email'] = forms.EmailInput(attrs={  # type: ignore
            'placeholder': 'Enter a valid email'
        })
        widgets['description'] = forms.Textarea(attrs={  # type: ignore
            'placeholder': 'Enter a description'})

        widgets['picture'] = forms.FileInput(attrs={  # type: ignore
            'accept': 'image/*', })

    def clean(self) -> dict[str, Any]:
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        msg_error_duplicate_value = ValidationError(
            'Error: duplicated value',)

        # this is a temporary error check
        if first_name == last_name:

            self.add_error('first_name', msg_error_duplicate_value
                           )

            self.add_error('last_name', msg_error_duplicate_value
                           )
        return super().clean()

    # def clean_name_of_field
    # this is a temporary error check
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error('first_name', ValidationError('ABC is not allowed'))

        return first_name
