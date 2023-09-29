from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

# class CustomerUserAdmin(UserAdmin):
#     add_form = UserCreationForm
#     form = UserChangeForm
#     model = todoUserProfile
#     list_display = ['pk','username','email','first_name','last_name']
#     add_fieldsets = UserAdmin.add_fieldsets +(
#         (None, {'fields': ('username','email','first_name','last_name',)}),
#     )
#     fieldsets = UserAdmin.add_fieldsets
# admin.site.register(todoUserProfile,CustomerUserAdmin)

# class TodoUser(admin.StackedInline):
#     model = Profiles

# class TodoUserAdmin(UserAdmin):
#     inlines = (TodoUser,)
# admin.site.unregister(User)
# admin.site.register(User,TodoUserAdmin)
# admin.site.register(Room)
# admin.site.register(theme)
# admin.site.register(Commentaires)
# admin.site.register(UserMessage)
# admin.site.register(Images)
# admin.site.register(ImagesProduct)
# admin.site.register(Profiles)






