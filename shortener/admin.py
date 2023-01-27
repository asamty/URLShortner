from django.contrib import admin

# Register your models here.
from shortener.models import Shortener
# Register your models here.

class ShortenerAdmin(admin.ModelAdmin):
    list_display = ('short_code','original_url', 'count', 'created_at')
    ordering = ('-created_at',)

admin.site.register(Shortener, ShortenerAdmin)