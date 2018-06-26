from django import forms
from django.core import validators


def check_for_a(value):
    if value[0].lower() != 'a':
        raise forms.ValidationError
        {"Name should start from A"}


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_a])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    verify_email = forms.EmailField[label = 'Enter your email again']
    #botcatcher = forms.CharField(required=False , widget = forms.HiddenInput validators=[validators.MaxlengthValidator(0)])


verify_email=forms.EmailField[label='Enter your email again']
    def clean(self):
        all_clean_data=super.clean()
        email=all_clean_data['email']
        vemail=all_clean_data['verify_mail']

        if email!=vemail:
            raise forms.validationError