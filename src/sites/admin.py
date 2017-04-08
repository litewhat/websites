from django.contrib import admin
from .models import Website, WebsiteCategory, WebPage

@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    pass


@admin.register(WebsiteCategory)
class WebsiteCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(WebPage)
class WebPageAdmin(admin.ModelAdmin):
    pass
