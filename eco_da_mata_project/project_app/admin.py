from django.contrib import admin
from .models import Project
from core.models import Image


class ImageInline(admin.TabularInline):
    model = Image
    
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Project, ProjectAdmin)
