from django.contrib import admin
from .models import Blog, BlogCategory
from unfold.admin import ModelAdmin
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(BlogCategory)
class BlogCategoryModelAdmin(ModelAdmin, ImportExportModelAdmin):
    pass


@admin.register(Blog)
class BlogModelAdmin(ModelAdmin, ImportExportModelAdmin):
    pass
