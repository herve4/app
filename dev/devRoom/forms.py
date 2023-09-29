# from django.forms import EmailInput, ImageField, ModelForm, PasswordInput, TextInput, Textarea
# from django.http import HttpResponse
# from devRoom.models import *
# from django.contrib.auth.forms import UserCreationForm
# from django import forms
# from django.contrib.auth.models import User
# from django.core.validators import RegexValidator
# from .models import Commentaires, todoUserProfile


# class CommentForm(ModelForm):
#     body = forms.Textarea()
 
#     class Meta:
#         model = Commentaires
#         fields = ['body']

#         widgets = {
#         'body':Textarea(attrs={
#         'type':'textarea',
#         'name':'comment',
#         'class':'form-control',
#         'id':'id_comment',
#         'label':'Message : ',
#         'placeholder':'Ecrire ici...',
#         'style':'background-color=#fff'
#         }),
       
#     }

# class roomForm(ModelForm):
    
#     # theme = forms.CharField(label='Catégorie',widget=forms.TextInput(attrs=
#     # {
#     # 'type':'text',
#     # 'name':'theme',
#     # 'class':'form-control',
#     # 'id':'id_theme',
#     # 'placeholder':'Créer une catégorie',
#     # 'required':True,

#     # }))

#     name = forms.CharField(label='Titre',widget=forms.TextInput(attrs=
#     {
#     'type':'text',
#     'name':'name',
#     'class':'form-control',
#     'id':'id_name',
#     'placeholder':'Créer un titre',
#     'required':True,

#     }))
#     # description = forms.Textarea(widget=forms.Textarea(attrs={
#     # 'type':'textarea',
#     # 'name':'description',
#     # 'class':'form-control',
#     # 'id':'id_description',
#     # 'placeholder':'Créer un titre',
#     # 'required':True,

#     # }))
    

#     class Meta:
#         model = Room
#         fields = ['name','description']

#         widgets = {
#         'description':Textarea(attrs={
#         'type':'textarea',
#         'name':'description',
#         'class':'form-control',
#         'id':'id_description',
#         'placeholder':'Description'
#         }),
       
#     }
        
# class TodoUserForm(ModelForm):
#     image = forms.ImageField(label='Image',widget=forms.FileInput(attrs=
#     {
#     'type':'file',
#     'name':'img',
#     'class':'form-control',
#     'id':'id_img',
#     'placeholder':'Image',
#     'required':False,

#     }))
#     class Meta:
#         model = Profiles

#         fields = ['Telephone','Fonctions','Experience','competence1','competence2','competence3','competence4','competence5','competence6','image']
       

#         widgets = {
#         'Telephone':TextInput(attrs={
#         'type':'text',
#         'name':'phone',
#         'class':'form-control',
#         'id':'id_phone',
#         'placeholder':'Téléphone',
#         'required':False,
#         }),
#         'Fonctions':TextInput(attrs={
#         'type':'text',
#         'name':'fonction',
#         'class':'form-control',
#         'id':'id_fonction',
#         'placeholder':'Fonction',
#         'required':False,
#         }),
#          'Experience':TextInput(attrs={
#         'type':'number',
#         'name':'Experience',
#         'class':'form-control',
#         'id':'id_Experience',
#         'placeholder':'Experience',
#         'required':False,
#         }),
#          'competence1':TextInput(attrs={
#         'type':'text',
#         'name':'comp1',
#         'class':'form-control',
#         'id':'id_comp1',
#         'placeholder':'Compétence 1',
#         'required':False,
#         }),
#           'competence2':TextInput(attrs={
#         'type':'text',
#         'name':'comp2',
#         'class':'form-control',
#         'id':'id_comp2',
#         'placeholder':'Compétence 2',
#         'required':False,
#         }),
#           'competence3':TextInput(attrs={
#         'type':'text',
#         'name':'comp3',
#         'class':'form-control',
#         'id':'id_comp3',
#         'placeholder':'Compétence 3',
#         'required':False,
#         }),
#           'competence4':TextInput(attrs={
#         'type':'text',
#         'name':'comp4',
#         'class':'form-control',
#         'id':'id_comp4',
#         'placeholder':'Compétence 4',
#         'required':False,
#         }),
#           'competence5':TextInput(attrs={
#         'type':'text',
#         'name':'comp5',
#         'class':'form-control',
#         'id':'id_comp5',
#         'placeholder':'Compétence 5',
#         'required':False,
#         }),
#           'competence6':TextInput(attrs={
#         'type':'text',
#         'name':'comp6',
#         'class':'form-control',
#         'id':'id_comp6',
#         'placeholder':'Compétence 6',
#         'required':False,
#         }),
#         # 'image':ImageField(label='Image')
       

       
#         }
#     # exclude = ['image']  

# class ImageForm(ModelForm):
#     fileUser = forms.ImageField(label='Image',widget=forms.FileInput(
#     {
#     'type':'file',
#     'name':'img',
#     'class':'form-control',
#     'id':'id_img',
#     'placeholder':'Image',
#     'required':True,

#     }))
#     class Meta:
#         model = Images
#         fields = ['fileUser','user']
        

# class infoUser(ModelForm):
     
#     account = forms.CharField(label='Nom',widget=forms.TextInput(
#     {
#     'type':'text',
#     'name':'todouserprofile-0-account',
#     'class':'form-control',
#     'id':'id_todouserprofile-0-Telephone',
#     'placeholder':'Nom',
#     'required':True,

#     }))

#     mobile_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$", message=" Format incorrect, nécessite un code de pays. Ex : +225070898786")
#     Telephone = forms.CharField(label='Telephone',widget=forms.TextInput(
#     {
#     'type':'phone',
#     'name':'todouserprofile-0-Telephone',
#     'class':'form-control',
#     'id':'id_todouserprofile-0-Telephone',
#     'placeholder':'EX: +2250708987867',
#     'required':True,

#     }
#         ),validators=(mobile_regex,))
#     class Meta:
#         model = todoUserProfile

       
        
#         fields = ['account','Telephone']
      
      
# class RegisterForm(UserCreationForm):

#     email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs=
#     {   
#         'type':'text',
#         'class':'form-control',
#         'id':'id_email',
#         'placeholder':'Email'
#     }                                                               
    
#     ))
#     # username = forms.CharField(label='Nom d\'utilisateur',widget=forms.TextInput(attrs=
#     # {
#     #     'class':'form-control',
#     #     'id':'id_register_form_fullname',
#     #     'placeholder':'Nom d\'utilisateur'
#     # }                                                               
    
#     # ))
    

#     password1 = forms.CharField(label='Mot de passe',widget=forms.PasswordInput(attrs={
#         'type':'password',
#         'name':'password1',
#         'class':'form-control',
#         'id':'id_password1',
#         'placeholder':'Mot de passe'
#     }))
#     password2 = forms.CharField(label='Confirmer votre mot de passe',widget=forms.PasswordInput(attrs={
#         'type':'password',
#         'name':'password2',
#         'class':'form-control',
#         'id':'id_password2',
#         'placeholder':'Confirmer votre mot de passe'
#     }))
    
#     class Meta:
#         model = User
#         fields = ['username','email','password1','password2']

#         widgets = {
#             'username':TextInput(attrs={
#             'type':'text',
#             'name':'username',
#             'class':'form-control',
#             'id':'id_username',
#             'placeholder':'Utilisateur'
#             }),
#             'email':EmailInput(attrs={
#             'type':'text',
#             'name':'email',
#             'class':'form-control',
#             'id':'id_email',
#             'placeholder':'Email'
#             }),
#             'password1':PasswordInput(attrs={
#             'type':'password',
#             'name':'password1',
#             'class':'form-control',
#             'id':'id_password1',
#             'placeholder':'Mot de passe'
#             }),
#             'password2':PasswordInput(attrs={
#             'type':'password',
#             'name':'password2',
#             'class':'form-control',
#             'id':'id_password2',
#             'placeholder':'Confirmer votre mot de passe'
#             }),
#         }


# class Utilisateur(forms.ModelForm):
#     email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs=
#     {
#         'class':'form-control',
#         'id':'id_register_form_email',
#         'placeholder':'Email'
#     }                                                               
    
#     ))
#     username = forms.CharField(label='Nom d\'utilisateur',widget=forms.TextInput(attrs=
#     {
#         'class':'form-control',
#         'id':'id_register_form_fullname',
#         'placeholder':'Nom d\'utilisateur'
#     }                                                               
    
#     ))
    

#     password1 = forms.CharField(label='Mot de passe',widget=forms.PasswordInput(attrs={
#         'type':'password',
#         'name':'password1',
#         'class':'form-control',
#         'id':'id_password1',
#         'placeholder':'Mot de passe'
#     }))
#     password2 = forms.CharField(label='Confirmer votre mot de passe',widget=forms.PasswordInput(attrs={
#         'type':'password',
#         'name':'password2',
#         'class':'form-control',
#         'id':'id_password2',
#         'placeholder':'Confirmer votre mot de passe'
#     }))
#     mobile_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$", message=" Format incorrect, nécessite un code de pays. Ex : +225070898786")
#     Telephone = forms.CharField(label='Telephone',widget=forms.TextInput(
#     {
#     'type':'phone',
#     'name':'todouserprofile-0-Telephone',
#     'class':'form-control',
#     'id':'id_todouserprofile-0-Telephone',
#     'placeholder':'EX: +2250708987867',
#     'required':True,

#     }
#         ),validators=(mobile_regex,))
   

#     # RoomInfoUser = forms.ModelChoiceField(queryset=todoUserProfile.objects.all())


#     # class Meta:
#     #     model = todoUserProfile
#     #     fields = ['username','email','Telephone','password1','passwoord2']