from django.contrib import admin
from .models import Home, Category, Contact, Client, Images
from import_export.admin import ImportExportModelAdmin
from unfold.admin import ModelAdmin

# Register your models here.


# Actions

@admin.action(description='Delete object')
def off_delete(modeladmin:admin.ModelAdmin, request, queryset):
    if request.user.is_superuser:
        queryset.update(is_delete = True)
        modeladmin.message_user(request, 'Success')
        
    else:
        modeladmin.message_user(request, 'You are not Superuser')
        

@admin.action(description='Reset obeject')
def reset_delete(modeladmin:admin.ModelAdmin, request, queryset):
    if request.user.is_superuser:
        queryset.update(is_delete = False)
        modeladmin.message_user(request, 'Success')
        
    else:
        modeladmin.message_user(request, 'You are not Superuser')


# Admin classes

class SuperClassModelAdmin(ImportExportModelAdmin, ModelAdmin):
    
    actions = [off_delete, reset_delete]
    
    def has_delete_permission(self, *args, **kwargs):
        return False
    
    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request).filter()
        else:
            return super().get_queryset(request).filter()


@admin.register(Category)
class CategoryModelAdmin(SuperClassModelAdmin):
    list_display = ['name', 'is_active']
    search_fields = ['name']
    
    
@admin.register(Home)
class HomeModelAdmin(SuperClassModelAdmin):
    list_display = ['name', 'city', 'size', 'price', 'is_new', 'status', 'category']
    search_fields = ['name', 'city', 'price', 'category']
    ordering = ['category', 'price', 'size', 'created_at']
    prepopulated_fields = {'slug' : ('name',)}
    

@admin.register(Images)
class ImagesModelAdmin(SuperClassModelAdmin):
    list_display = ['name', 'image', 'home']
    search_fields = ['name', 'home']
    ordering = ['home']



@admin.register(Contact)
class ContactModelAdmin(SuperClassModelAdmin):
    list_display = ['phone', 'email', 'address']
    search_fields = ['phone', 'email', 'address']
    
    
    def has_add_permission(self, request):
        if Contact.objects.exists():
            return False
        return super().has_add_permission(request)



@admin.register(Client)
class ClientModelAdmin(SuperClassModelAdmin):
    list_display = ['name', 'profession',]
    


