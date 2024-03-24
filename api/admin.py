from django.contrib import admin
from .models import HandbookCategory, HandbookEntry

@admin.register(HandbookCategory)
class HandbookCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(HandbookEntry)
class HandbookEntryAdmin(admin.ModelAdmin):
    list_display = ('category', 'title')
    list_filter = ('category',)
    search_fields = ('title', 'content')
    