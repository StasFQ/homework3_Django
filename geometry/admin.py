from django.contrib import admin

from .models import Logs


class LogsAdmin(admin.ModelAdmin):
    list_display = ['path', 'method', 'time']
    list_filter = ['time']
    search_fields = ['path']
    date_hierarchy = 'time'
    ordering = ['time']


admin.site.register(Logs, LogsAdmin)
