from django.contrib import admin
from .models import Project, ProjectImage, ContactMessage
from django.utils.html import format_html

class ProjectImageInline(admin.TabularInline):   # или StackedInline
    model = ProjectImage
    extra = 1   # сколько пустых полей для загрузки показывать
    fields = ('image', 'order')
    ordering = ('order',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'icon', 'order', 'is_active', 'created_at')
    list_display_links = ('id', 'title')
    list_editable = ('icon', 'order', 'is_active')
    search_fields = ('title', 'description')
    list_filter = ('is_active', 'icon')
    fields = ('title', 'description', 'icon', 'order', 'is_active', 'cover_title', 'image', 'created_at')
    readonly_fields = ('created_at',)
    inlines = [ProjectImageInline]   # добавляем

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'created_at', 'is_read')
    list_display_links = ('id', 'name')
    list_editable = ('is_read',)
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('is_read', 'created_at')
    readonly_fields = ('created_at',)