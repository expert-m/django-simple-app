from django.contrib import admin
from core.models import Region, Customer, Provider


class CustomerAdmin(admin.ModelAdmin):
    fields = ('name', 'regions',)
    list_display = ('name',)


class ProviderAdmin(admin.ModelAdmin):
    fields = ('name', 'regions',)
    list_display = ('name',)


admin.site.register(Region)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Provider, ProviderAdmin)
