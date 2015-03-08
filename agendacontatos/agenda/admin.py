from models import ItemAgenda
from django.contrib import admin

class ItemAgendaAdmin(admin.ModelAdmin):
    fields = ('nome', 'email', 'telefone1', 'telefone2', 'endereco')
    list_display =('nome', 'email', 'telefone1')

    def queryset(self, request):
        qs = super(ItemAgendaAdmin, self).queryset(request)
        return qs.filter(usuario=request.user)

    def save_model(self, request, obj, form, change):
        obj.usuario =request.user
        obj.save()

admin.site.register(ItemAgenda, ItemAgendaAdmin)