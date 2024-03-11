from django.contrib import admin
from . models import Items
from . forms import ItemCreateForm

# Register your models here.

class ItemCreateAdmin(admin.ModelAdmin):
    list_display = ['category','item_name','quantity_of_packs']
    form = ItemCreateForm
    list_filter = ['category']
    search_fields = ['category','item_name']

admin.site.register(Items,ItemCreateAdmin)
