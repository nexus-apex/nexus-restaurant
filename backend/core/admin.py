from django.contrib import admin
from .models import MenuItem, TableOrder, DiningTable

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "price", "cost", "status", "created_at"]
    list_filter = ["category", "status", "spice_level"]
    search_fields = ["name"]

@admin.register(TableOrder)
class TableOrderAdmin(admin.ModelAdmin):
    list_display = ["table_number", "server", "items_count", "subtotal", "tax", "created_at"]
    list_filter = ["status", "payment"]
    search_fields = ["table_number", "server"]

@admin.register(DiningTable)
class DiningTableAdmin(admin.ModelAdmin):
    list_display = ["table_number", "capacity", "section", "status", "reserved_name", "created_at"]
    list_filter = ["section", "status"]
    search_fields = ["table_number", "reserved_name"]
