from django.contrib import admin
from .models import Profile,Category,Subcategory,Uploadpets,User,Contact

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

class ProfileAdmin(admin.ModelAdmin):
    list_editable = ['verified']
    list_display = ['user','first_name','last_name','address','verified']
    
class UserAdmin(admin.ModelAdmin):
    list_display =['email','username']
    
admin.site.register(Profile,ProfileAdmin)
admin.site.register(User,UserAdmin)

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Uploadpets,ProductAdmin)
admin.site.register(Contact)

