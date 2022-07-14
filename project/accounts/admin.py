from django.contrib import admin
from .models import Customer, User , Permission, User_Permission
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .forms import MyUserCreationForm, MyUserChangeForm


class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = User
    list_display = ['username', 'is_staff', 'is_superuser','is_active']
    fieldsets = (
        ('standard info' , {
            'description': 'These fields are required for each',
            'fields':('username' , 'password')
        }),
        ( 'managers' ,{
            'classes': ('collapse',),
            'fields':(('is_superuser', 'is_staff' ),( 'is_active' ))
        }),
        ( 'permission' ,{
            'fields':(('date_joined','last_login') )
        }),


    )
    filter_horizontal = ()
    list_filter = ('is_staff', 'is_superuser', 'is_active',)

admin.site.register(User, MyUserAdmin)

admin.site.register(Permission )
admin.site.unregister(Group)



class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ('id_number',)


admin.site.register(Customer,CustomerAdmin)



class PermissionAdmin(admin.ModelAdmin):
    list_display = ['user' , 'per_user' ,'is_confermid']


admin.site.register(User_Permission ,PermissionAdmin )
