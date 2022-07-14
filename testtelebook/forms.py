from django import forms
from .models import ContactInPhone, TypesInPhone


class AddNameContact(forms.ModelForm):
    class Meta:
        model = ContactInPhone
        fields = '__all__'


class AddTypeContact(forms.ModelForm):
    class Meta:
        model = TypesInPhone
        fields = '__all__'









