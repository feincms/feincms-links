from django import forms
from django.conf import settings
from django.contrib import admin

from .models import Category, Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'url', 'category',)
    list_filter = ('category',)


class LinkOrderForm(forms.ModelForm):
    model = Link

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.5.0/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.9/jquery-ui.min.js',
            settings.STATIC_URL + 'feincms_links/move-order.js',
        )

class LinkAdminInline(admin.StackedInline):
    model = Link
    form = LinkOrderForm
    extra = 1


class LinkCategoryAdmin(admin.ModelAdmin):
    model = Category
    inlines = [LinkAdminInline]


admin.site.register(Link, LinkAdmin)
admin.site.register(Category, LinkCategoryAdmin)
