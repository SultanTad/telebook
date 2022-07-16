import django_filters
from .models import ContactInPhone


class TeleBookFilter(django_filters.FilterSet):
    class Meta:
        model = ContactInPhone
        fields = '__all__'
