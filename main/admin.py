from django.contrib import admin
from .models import Home, Category, Contact, Client
from import_export.admin import ImportExportModelAdmin
from unfold.admin import ModelAdmin

# Register your models here.

@admin.register(Category)
class CategoryModelAdmin(ModelAdmin, ImportExportModelAdmin):
    pass    


@admin.register(Home)
class HomeModelAdmin(ModelAdmin, ImportExportModelAdmin):
    pass    


@admin.register(Contact)
class ContactModelAdmin(ModelAdmin, ImportExportModelAdmin):
    
    
    def has_add_permission(self, request):
        if Contact.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(Client)
class ClientModelAdmin(ModelAdmin, ImportExportModelAdmin):
    pass  


