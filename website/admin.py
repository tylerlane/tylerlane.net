from django.contrib import admin
from models import import Page

class PageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Page,PageAdmin)
