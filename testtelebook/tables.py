import django_tables2 as tables
from .models import ContactInPhone


class TeleBookTable(tables.Table):
    class Meta:
        model = ContactInPhone
        template_name = 'django_tables2/semantic.html'
        fields = '__all__'
