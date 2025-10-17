from django.contrib import admin
from .models import Home, Category
from import_export.admin import ImportExportModelAdmin
from unfold.admin import ModelAdmin

# Register your models here.

@admin.register(Category)
class CategoryModelAdmin(ModelAdmin, ImportExportModelAdmin):
    pass    


@admin.register(Home)
class HomeModelAdmin(ModelAdmin, ImportExportModelAdmin):
    pass    


