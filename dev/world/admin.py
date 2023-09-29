from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from world.models import *
from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

# Supprimer le modèle de groupe de l'administrateur. Nous ne l'utilisons pas.
#admin.site.unregister(Group)

# class UserAdmin(BaseUserAdmin):
#     # Les formulaires pour ajouter et modifier des instances d'utilisateur
#     form = UserAdminChangeForm
#     add_form = UserAdminCreationForm

#     # Les champs à utiliser pour afficher le modèle User.
#     # Celles-ci remplacent les définitions de la baseUserAdmin
#     # qui font référence à des champs spécifiques sur auth.User.
#     list_display = ['email','phone', 'admin','staff']
#     list_filter = ['admin']
#     fieldsets = (
#     (None, {'fields': ('email','phone','password',)}),
#     ('Infos personnelles', {'fields': ()}),
#     ('Permissions', {'fields': ('staff','is_active','admin',)}),
#     ('Autres infos',{'fields': ('last_login',)})
#     )
#     # add_fieldsets n'est pas un attribut ModelAdmin standard. UtilisateurAdmin
#     # remplace get_fieldsets pour utiliser cet attribut lors de la création d'un utilisateur.
#     add_fieldsets = (
#     (None, {
#     'classes': ('wide',),
#     'fields': ('email', 'password', 'password_2')}
#     ),
#     )
#     search_fields = ['email']
#     ordering = ['email']
#     filter_horizontal = ()


# admin.site.register(User, UserAdmin)


class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        (_('Informations personnelles'), {'fields': ('first_name', 'last_name','fonction','Telephone','image','adresse','Experience', 'competence1','competence2','competence3','competence4','competence5','competence6')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Dates utilisateur'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('username','email', 'is_staff','fonction','Telephone')
    search_fields = ('email', 'username', 'last_name')
    ordering = ('username','email',)


admin.site.register(get_user_model(), CustomUserAdmin)
admin.site.register(Sujets)
admin.site.register(MessagesUser)
admin.site.register(Commentaires)
admin.site.site_header = 'GraffitikDev'
admin.site.site_title = 'Chambre du développeur'
admin.site.index_title = 'Manager'