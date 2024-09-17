from typing import Any
from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'This is forms.charfield'
        }),
        label='Your first name',
        help_text='A help text for your user'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'placeholder': This is INIT',
        #     'class': 'class1 class2',
        # }
        # )

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'phone')
        # widgets = {
        #     'first_name': forms.TextInput(attrs={
        #         'class': 'classeaA classeB',
        #         'placeholder': 'This is widgets'
        #     }),
        #     'email': forms.EmailInput()
        # }

    def clean(self) -> dict[str, Any]:
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        msg_error_duplicate_value = ValidationError(
            'Não pode ser igual',)

        if first_name == last_name:

            self.add_error('first_name', msg_error_duplicate_value
                           )

            self.add_error('last_name', msg_error_duplicate_value
                           )
        return super().clean()

    # def clean_name_of_field
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error('first_name', ValidationError('Não pode ABC'))

        return first_name
