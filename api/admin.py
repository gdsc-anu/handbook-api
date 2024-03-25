from django.contrib import admin
from .models import HandbookCategory, HandbookEntry

class HandbookEntryInline(admin.StackedInline):
    model = HandbookEntry
    extra = 0

@admin.register(HandbookCategory)
class HandbookCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

    inlines = [HandbookEntryInline]

@admin.register(HandbookEntry)
class HandbookEntryAdmin(admin.ModelAdmin):
    list_display = ('category', 'title')
    list_filter = ('category',)
    search_fields = ('title', 'content')

    actions = ['archive_entries']

    def archive_entries(self, request, queryset):
        queryset.update(archived=True)
    archive_entries.short_description = "Archive selected entries"
