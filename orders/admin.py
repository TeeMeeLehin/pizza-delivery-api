from django.contrib import admin
from .models import order


@admin.register(order)
class orderAdmin(admin.ModelAdmin):
    list_display = ['size', 'order_status', 'quantity', 'created_at']
    list_filter = ['size', 'order_status', 'quantity', 'created_at']