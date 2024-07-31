from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Email Address'
        }),
        error_messages={
            'required': 'Email Address is required.',
            'invalid': 'Email Address Email is not valid.'
        }
    )
