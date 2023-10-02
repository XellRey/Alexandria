from django import forms
from main.models import Books


class CartAddProductForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = []