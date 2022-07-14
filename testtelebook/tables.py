import django_tables2 as tables
from .models import TypesInPhone


class TeleBookTable(tables.Table):
    class Meta:
        model = TypesInPhone
        template_name = 'django_tables2/semantic.html'
        fields = '__all__'
