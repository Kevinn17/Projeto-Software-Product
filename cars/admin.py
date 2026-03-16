from django.contrib import admin
from cars.models import Car, Marca

class CarAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'marca', 'fabricado_em', 'ano_modelo', 'valor')
    search_fields = ('modelo','marca')

class BranAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Car, CarAdmin)
admin.site.register(Marca, BranAdmin)
