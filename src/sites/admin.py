from django.contrib import admin
from .models import Website, WebPage


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    pass


@admin.register(WebPage)
class WebPageAdmin(admin.ModelAdmin):
    pass
