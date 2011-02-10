from django.contrib import admin

from models import Category, Link

class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'url', 'category',)
    list_filter = ('category',)
    
admin.site.register(Link, LinkAdmin)
admin.site.register(Category)