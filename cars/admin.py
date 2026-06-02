from django.contrib import admin
from cars.models import Car, Marca, Agendamento

class CarAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'marca', 'fabricado_em', 'ano_modelo', 'valor')
    search_fields = ('modelo','marca')

class BranAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('nome_cliente', 'carro', 'data_hora', 'tipo', 'status')
    list_filter = ('status', 'tipo', 'data_hora')
    
admin.site.register(Car, CarAdmin)
admin.site.register(Marca, BranAdmin)
admin.site.register(Agendamento, AgendamentoAdmin)
