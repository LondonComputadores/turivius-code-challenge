from django.contrib import admin
from court_app.models import Lawsuits

class Lawsuit(admin.ModelAdmin):
    list_display = ('id', 'lawsuit_number', 'summarization')
    list_display_links = ('id', 'lawsuit_number')
    search_fields = ('lawsuit_number',)

admin.site.register(Lawsuits, Lawsuit)