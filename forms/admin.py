from django.contrib import admin

from .models import Logs


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ['path', 'method', 'has_get_data', 'has_post_data', 'timestamp']
    list_filter = ['timestamp', 'method']
    search_fields = ['path__contains']
    date_hierarchy = 'timestamp'
