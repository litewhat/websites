from django.contrib import admin
from .models import WebsiteCategory


@admin.register(WebsiteCategory)
class WebsiteCategoryAdmin(admin.ModelAdmin):
    pass
