import django_filters
from .models import TypesInPhone


class TeleBookFilter(django_filters.FilterSet):
    class Meta:
        model = TypesInPhone
        fields = '__all__'
