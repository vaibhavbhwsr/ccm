from django.contrib import admin
from core.models import Case, Invoice, Contact

# Register your models here.


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'number', 'case_type', 'case_status', 'lawyer', 'client'
    )


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('case', 'amount', 'client', 'lawyer')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'about')
