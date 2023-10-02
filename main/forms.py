from django import forms
from main.models import ContactMessage


class ContactMessage(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['email', 'name', 'subject', 'message']

        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'name': forms.TextInput(attrs={'placeholder': 'name'}),
            'subject': forms.TextInput(attrs={'placeholder': 'subject'}),
            'message': forms.Textarea(attrs={'placeholder': 'message'}),
        }


