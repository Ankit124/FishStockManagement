from django.contrib import admin
from .models import Stock
from .forms import StockCreateForm


class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['species', 'name', 'quantity','length','latitude','longitude', 'timestamp']
    form = StockCreateForm
    list_filter = ['species']
    search_fields = ['species', 'name']


admin.site.register(Stock, StockCreateAdmin)