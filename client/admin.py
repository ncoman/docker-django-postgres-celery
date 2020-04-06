from django.contrib import admin

from client.models import Contact, Company, Client


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'account_type',)
    ordering = ('name', 'account_type',)
    search_fields = ('name',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email',)
    ordering = ('name', 'phone', 'email',)
    search_fields = ('name',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'company_name', 'contact', 'key',)
    ordering = ('name', 'company',)
    list_filter = ('company', 'contact',)
    search_fields = ('name',)
    # list_editable = ['key']


    def company_name(self, obj):
        if obj.company is not None:
            return f"{obj.company.name}"

