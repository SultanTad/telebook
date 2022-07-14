from django.contrib import admin
from .models import *


class TypesInline(admin.TabularInline):
    model = TypesInPhone


class ContactAdmin(admin.ModelAdmin):
    inlines = [
        TypesInline,
    ]


admin.site.register(ContactInPhone, ContactAdmin)
admin.site.register(TypesInPhone)


