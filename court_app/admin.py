from django.contrib import admin
from court_app.models import Lawsuit

class Lawsuits(admin.ModelAdmin):
    list_display = ('n_processo','id_cliente', 'favor_contribuinte', 'ementa')
    list_display_links = ('n_processo', 'id_cliente')
    search_fields = ('n_processo',)

admin.site.register(Lawsuit, Lawsuits)