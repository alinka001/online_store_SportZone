from django import forms
from .models import ItemTag


class ItemTagForm(forms.ModelForm):
    class Meta:
        model = ItemTag
        fields = ['name', 'image', 'description']
