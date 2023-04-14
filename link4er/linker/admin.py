from django.contrib import admin
from .models import RedirectLink

class RedirectLinkAdmin(admin.ModelAdmin):
    fields = ['redirect', 'to']

admin.site.register(RedirectLink, RedirectLinkAdmin)
