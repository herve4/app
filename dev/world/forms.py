from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import *


from world.models import *
User = get_user_model()

class loginForm(forms.ModelForm):
    # email = forms.CharField(label='Adresse Email',widget=forms.EmailInput(attrs={ 
    #             'type':'text',
    #             'class':'form-control',
    #             'required':True,}))
    # password = forms.CharField(label='Mot de passe',widget=forms.PasswordInput(attrs={ 
    #         'type':'password',
    #         'class':'form-control',
    #         'required':True,}))
    class Meta:
        model = User
        fields =['image'] 
    
    

        

class ProfilForm(forms.ModelForm):
    """
    The default

    """
    # image = forms.ImageField(label='Photo de profil',widget=forms.ImageField)
    # password = forms.CharField(label='Mot de passe',widget=forms.PasswordInput(attrs={'type':'password','class':'form-control'}))
    # password_2 = forms.CharField(label='Confirmer votre mot de passe', widget=forms.PasswordInput(attrs={'type':'password','class':'form-control'}))

    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={
                'type':'text',
                'class':'form-control',
                
            }),
            'username': forms.EmailInput(attrs={
                'type':'text',
                'class':'form-control',
                'required':False,
            }),
            'first_name':forms.TextInput(attrs={
        'type':'text',
        'name':'first_name',
        'class':'form-control',
        'id':'id_first_name',
        'placeholder':'Nom',
        'required':False,
        }),
        'last_name':forms.TextInput(attrs={
        'type':'text',
        'name':'last_name',
        'class':'form-control',
        'id':'id_last_name',
        'placeholder':'Prénom',
        'required':False,
        }),
        
        'Telephone':forms.TextInput(attrs={
        'type':'text',
        'name':'phone',
        'class':'form-control',
        'id':'id_phone',
        'placeholder':'Téléphone',
        'required':False,
        }),
        'adresse':forms.TextInput(attrs={
        'type':'text',
        'name':'adresse',
        'class':'form-control',
        'id':'id_adresse',
        'placeholder':'Adresse',
        'required':False,
        }),
        'fonction':forms.TextInput(attrs={
        'type':'text',
        'name':'fonction',
        'class':'form-control',
        'id':'id_fonction',
        'placeholder':'Fonction',
        'required':False,
        'label':'Fonction',
        }),
         'Experience':forms.TextInput(attrs={
        'type':'number',
        'name':'Experience',
        'class':'form-control',
        'id':'id_Experience',
        'placeholder':'Experience',
        'required':False,
        }),
         'competence1':forms.TextInput(attrs={
        'type':'text',
        'name':'comp1',
        'class':'form-control',
        'id':'id_comp1',
        'placeholder':'Compétence 1',
        'required':False,
        }),
          'competence2':forms.TextInput(attrs={
        'type':'text',
        'name':'comp2',
        'class':'form-control',
        'id':'id_comp2',
        'placeholder':'Compétence 2',
        'required':False,
        }),
          'competence3':forms.TextInput(attrs={
        'type':'text',
        'name':'comp3',
        'class':'form-control',
        'id':'id_comp3',
        'placeholder':'Compétence 3',
        'required':False,
        }),
          'competence4':forms.TextInput(attrs={
        'type':'text',
        'name':'comp4',
        'class':'form-control',
        'id':'id_comp4',
        'placeholder':'Compétence 4',
        'required':False,
        }),
          'competence5':forms.TextInput(attrs={
        'type':'text',
        'name':'comp5',
        'class':'form-control',
        'id':'id_comp5',
        'placeholder':'Compétence 5',
        'required':False,
        }),
          'competence6':forms.TextInput(attrs={
        'type':'text',
        'name':'comp6',
        'class':'form-control',
        'id':'id_comp6',
        'placeholder':'Compétence 6',
        'required':False,
        }),
          'image':forms.FileInput(attrs={
        'type':'file',
        'name':'image',
        'class':'form-control',
        'id':'id_image',
        'label':'Photo de profil',
        'required':False,
        }),
        # 'image':ImageField(label='Image')
       

       
        }

        exclude = ['is_active','is_superuser','groups','is_staff','password','first_name','last_name','user_permissions','date_joined','last_login']

    def clean_email(self):
        '''
        Verify email is available.
        '''
        email = self.cleaned_data.get('email')
       
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("L'e-mail existe déjà")
        return email
    # def clean_phone(self):
    #     '''
    #     Verifie si numero est disponible.
    #     '''
      
    #     phone = self.cleaned_data.get('phone')
    #     qs = User.objects.filter(phone=phone)
    #     if qs.exists():
    #         raise forms.ValidationError("Ce numéro existe déjà")
    #     return phone

    def clean(self):
        '''
        Vérifiez que les deux mots de passe correspondent.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
            return cleaned_data


class UserAdminCreationForm(forms.ModelForm):
    """
    Un formulaire pour créer de nouveaux utilisateurs. Comprend tout le nécessaire
    champs, plus un mot de passe répété.
    """
    password = forms.CharField(label='Mot de passe',widget=forms.PasswordInput(attrs={'type':'password','class':'form-control'}))
    password_2 = forms.CharField(label='Confirmer votre mot de passe', widget=forms.PasswordInput(attrs={'type':'password','class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','email']
        widgets = {
            'username': forms.TextInput(attrs={
                'type':'text',
                'class':'form-control',
            }),
           
            'email': forms.EmailInput(attrs={
                'type':'text',
                'class':'form-control',
            }),
        }
    def clean(self):
        '''
        Vérifiez que les deux mots de passe correspondent.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
            return cleaned_data

    def save(self, commit=True):
        # Enregistrez le mot de passe fourni au format haché
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            return user




class InscriptFormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','first_name','last_name']

        widgets = {
          'email': forms.EmailInput(attrs={
            'type':'email',
            'class':'form-control',
        }),
        'first_name': forms.TextInput(attrs={
            'type':'text',
            'class':'form-control',
        }),
        'last_name': forms.TextInput(attrs={
            'type':'text',
            'class':'form-control',
        })
       
        }
# class RoomUserForm(forms.ModelForm):
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

#         fields = ['Telephone','fonction','Experience','competence1','competence2','competence3','competence4','competence5','competence6','image']
       

#         widgets = {
#         'Telephone':forms.TextInput(attrs={
#         'type':'text',
#         'name':'phone',
#         'class':'form-control',
#         'id':'id_phone',
#         'placeholder':'Téléphone',
#         'required':False,
#         }),
#         'fonction':forms.TextInput(attrs={
#         'type':'text',
#         'name':'fonction',
#         'class':'form-control',
#         'id':'id_fonction',
#         'placeholder':'Fonction',
#         'required':False,
#         'label':'Fonction',
#         }),
#          'Experience':forms.TextInput(attrs={
#         'type':'number',
#         'name':'Experience',
#         'class':'form-control',
#         'id':'id_Experience',
#         'placeholder':'Experience',
#         'required':False,
#         }),
#          'competence1':forms.TextInput(attrs={
#         'type':'text',
#         'name':'comp1',
#         'class':'form-control',
#         'id':'id_comp1',
#         'placeholder':'Compétence 1',
#         'required':False,
#         }),
#           'competence2':forms.TextInput(attrs={
#         'type':'text',
#         'name':'comp2',
#         'class':'form-control',
#         'id':'id_comp2',
#         'placeholder':'Compétence 2',
#         'required':False,
#         }),
#           'competence3':forms.TextInput(attrs={
#         'type':'text',
#         'name':'comp3',
#         'class':'form-control',
#         'id':'id_comp3',
#         'placeholder':'Compétence 3',
#         'required':False,
#         }),
#           'competence4':forms.TextInput(attrs={
#         'type':'text',
#         'name':'comp4',
#         'class':'form-control',
#         'id':'id_comp4',
#         'placeholder':'Compétence 4',
#         'required':False,
#         }),
#           'competence5':forms.TextInput(attrs={
#         'type':'text',
#         'name':'comp5',
#         'class':'form-control',
#         'id':'id_comp5',
#         'placeholder':'Compétence 5',
#         'required':False,
#         }),
#           'competence6':forms.TextInput(attrs={
#         'type':'text',
#         'name':'comp6',
#         'class':'form-control',
#         'id':'id_comp6',
#         'placeholder':'Compétence 6',
#         'required':False,
#         }),
#         # 'image':ImageField(label='Image')
       

       
#         }

class UserAdminChangeForm(forms.ModelForm):
    """Un formulaire pour mettre à jour les utilisateurs. Inclut tous les champs sur
    l'utilisateur, mais remplace le champ du mot de passe par celui de l'administrateur
    champ d'affichage du hachage du mot de passe.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['email', 'password', 'is_active', 'is_superuser']

    def clean_password(self):
        # Indépendamment de ce que l'utilisateur fournit, renvoie la valeur initiale.
        # Cela se fait ici, plutôt que sur le terrain, car le
        # le champ n'a pas accès à la valeur initiale
        return self.initial["password"]
    
class RegisterFormUser(UserCreationForm):

    class Meta:
        model = User
        fields = ['email']
        widgets = {
        'email': forms.EmailInput(attrs={
            'type':'text',
            'class':'form-control',
        }),
        'password2': forms.PasswordInput(attrs={
            'type':'password',
            'class':'form-control',
        })
    }
        
class SujetForm(forms.ModelForm):
    
    class Meta:
        model = Sujets
        fields = ['theme','name','description','image','participate']
    #     fieldsets = (
    #     (None, {'fields': ('theme', 'name','description','image')}),
    #     (('Ajouter un participant à ce sujet'), {'fields': ('participants')}),
        
    # )

        widgets = {
        'theme': forms.TextInput(attrs={
        'type':'text',
        'class':'form-control',
        'name':'theme',
        'label':'Catégorie',
        'placeholder':'Catégorie',
        }),
        'name': forms.TextInput(attrs={
            'type':'text',
            'class':'form-control',
            'name':'titre',
            'label':'Titre du sujet',
            'placeholder':'Titre du sujet',
        }),
        'description': forms.Textarea(attrs={
            'type':'text',
            'class':'form-control',
            'name':'description',
            'label':'Description',
            'placeholder':'Description',
        }),
        'image': forms.FileInput(attrs={
            'type':'file',
            'class':'form-control',
            'name':'image',
            'label':'Image',
        }),
     
       
    }
        

       

class CommentForm(forms.ModelForm):
    body = forms.Textarea()
    
 
    class Meta:
        model = Commentaires
        fields = ['body']

        widgets = {
        'body':forms.Textarea(attrs={
        'type':'textarea',
        'name':'comment',
        'class':'form-control',
        'id':'id_comment',
        'label':'Message : ',
        'placeholder':'Ecrire ici...',
        'style':'background-color=#fff'
        }), 
    }