from django import forms
from .models import ContactInPhone, TypesInPhone


class AddNameContact(forms.ModelForm):
    class Meta:
        model = ContactInPhone
        fields = '__all__'










