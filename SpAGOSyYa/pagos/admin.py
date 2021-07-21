from django.contrib import admin
from .models import PagoSolicitado, PagosListado, State
# Register your models here.
class StateAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class SolicitadoAdmin(admin.ModelAdmin):
    readonly_fields = ('emision', 'updated')
    class Meta:
        model = PagoSolicitado



class LIstadoAdmin(admin.ModelAdmin):
    ordering = ('created', 'cantidad')


admin.site.register(State, StateAdmin)
admin.site.register(PagoSolicitado, SolicitadoAdmin)
admin.site.register(PagosListado, LIstadoAdmin)