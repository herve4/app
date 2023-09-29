# import filecmp
# from django.db import models
# from django.contrib.auth import get_user_model
# from phonenumber_field.modelfields import PhoneNumberField
# from django.db import models
# from django.contrib.auth.models import (
#     BaseUserManager, AbstractBaseUser
# )






# class UserManager(BaseUserManager):

#     def create_user(self, email, password=None):
#         """ Crée et enregistre un utilisateur avec l'e-mail et le mot de passe donnés."""
#         if not email:
#             raise ValueError('Les utilisateurs doivent avoir une adresse e-mail')

#         user = self.model(
#         email=self.normalize_email(email),
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user


#     def create_staffuser(self, email, password):
#         """
#         Crée et enregistre un utilisateur du staff avec l'e-mail et le mot de passe donnés.
#         """
#         user = self.create_user(
#         email,
#         password=password,
#         )
#         user.staff = True
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password):
#         """
#         Crée et enregistre un superutilisateur avec l'e-mail et le mot de passe donnés.
#         """
#         user = self.create_user(
#         email,
#         password=password,
#         )
#         user.staff = True
#         user.admin = True
#         user.save(using=self._db)
#         return user




# # accrochez le nouveau gestionnaire à notre modèle
# class User(AbstractBaseUser):
#     objects = UserManager()
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#     )
#     is_active = models.BooleanField(default=True)
#     staff = models.BooleanField(default=False) # a admin user; non super-user
#     admin = models.BooleanField(default=False) # a superuser
#     # remarquez l'absence du "champ password", c'est intégré pas besoin de preciser.
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = [] # Email & Password sont requis par défaut.
#     def get_full_name(self):
#         # L'utilisateur est identifié par son adresse e-mail
#         return self.email
#     def get_short_name(self):
#         # L'utilisateur est identifié par son adresse e-mail
#         return self.email
#     def __str__(self):
#         return self.email
#     def has_perm(self, perm, obj=None):
#         "L'utilisateur a-t-il une autorisation spécifique ?"
#         # Réponse la plus simple possible : Oui, toujours
#         return True
#     def has_module_perms(self, app_label):
#         "L'utilisateur dispose-t-il des autorisations nécessaires pour voir l'application ?`app_label`?"
#         # Réponse la plus simple possible : Oui, toujours
#         return True
#     @property
#     def is_staff(self):
#         "L'utilisateur est-il un membre du personnel ?"
#         return self.staff
#     @property
#     def is_admin(self):
#         "L'utilisateur est-il un membre administrateur?"
#         return self.admin







# class theme(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,verbose_name='Utilsateur')
#     name = models.CharField(max_length=200)
#     def __str__(self) -> str:
#         return self.name
#     class Meta:
#         verbose_name ='Thème'
#         verbose_name_plural = 'Thèmes'



# class Room(models.Model):
#     host = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Utilsateur')
#     theme = models.ForeignKey(theme, on_delete=models.CASCADE,verbose_name='Thème')
#     name = models.CharField(max_length=60,verbose_name='Titre')
#     description = models.TextField(verbose_name='Description',max_length=1000)
#     participants = models.ManyToManyField(User, related_name='Participants',null=True,blank=True)
#     created = models.DateTimeField(auto_now=True)
#     update = models.DateTimeField(auto_now_add=True)
#     def __str__(self) -> str:
#         return self.name
#     class Meta:
#         ordering = ['-created','-update']
#         verbose_name ='Titre'
#         verbose_name_plural = 'Titres'

# class Commentaires(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Utilisateur')
#     room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Titre')
#     theme = models.ForeignKey(theme, on_delete=models.CASCADE, verbose_name='Thème')
#     body = models.TextField(max_length=1000,verbose_name='Message')
#     creat = models.DateTimeField(auto_now=True)
#     mod = models.DateTimeField(auto_now_add=True)

#     def __str__(self) -> str:
#         return self.body[0:50]
#     class Meta:
#         ordering = ['-creat','-mod']
#         verbose_name ='Commentaire'
#         verbose_name_plural = 'Commentaires'

# class UserMessage(models.Model):
#     name = models.TextField(max_length=2000,verbose_name='Messages utilisateur')
#     user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Utilisateur',null=True,blank=True)
#     room = models.ForeignKey(Room,on_delete=models.CASCADE,verbose_name='Titres sujets',null=True,blank=True)
#     theme = models.ForeignKey(theme, on_delete=models.CASCADE,verbose_name='Thèmes',null=True,blank=True)
#     created = models.DateTimeField(auto_now=True,verbose_name='Publié')
#     update = models.DateTimeField(auto_now_add=True,verbose_name='Modifié')
#     def __str__(self) -> str:
#         return self.name[0:50]
#     class Meta:
#         ordering = ['-created','-update']
#         verbose_name = 'Message'
#         verbose_name_plural = 'Messages'

# class Images(models.Model):
#     fileUser = models.ImageField(upload_to='media',verbose_name='Images utilisateurs',max_length=255,null=True,blank=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Utilisateur',null=True,blank=True)
#     created = models.DateTimeField(auto_now=True,verbose_name='Publié')
#     update = models.DateTimeField(auto_now_add=True,verbose_name='Modifié')


#     class Meta:
        
#         verbose_name = 'Image'
#         verbose_name_plural = 'Images'

# class ImagesProduct(models.Model):
#     fileSujet = models.ImageField(upload_to='media',verbose_name='Images sujets',max_length=255,null=True,blank=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Utilisateur',blank=True)
#     room = models.ForeignKey(Room,on_delete=models.CASCADE,verbose_name='Titres sujets',null=True,blank=True)
#     theme = models.ForeignKey(theme, on_delete=models.CASCADE,verbose_name='Thèmes',null=True,blank=True)
#     created = models.DateTimeField(auto_now=True,verbose_name='Publié')
#     update = models.DateTimeField(auto_now_add=True,verbose_name='Modifié')
#     def __str__(self) -> str:
#         return self.fileSujet
#     class Meta:
        
#         verbose_name = 'Image Produit'
#         verbose_name_plural = 'Images Produits'
# class todoUserProfile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
#     Telephone = PhoneNumberField(max_length=14,null=True,blank=True, unique=True)
#     fonction = models.CharField(max_length=45,null=True,blank=True)
#     Experience = models.IntegerField(null=True,blank=True)
#     competence1 = models.CharField(max_length=35,verbose_name='Compétence 1',null=True,blank=True)
#     competence2 = models.CharField(max_length=35,verbose_name='Compétence 2',null=True,blank=True)
#     competence3 = models.CharField(max_length=35,verbose_name='Compétence 3',null=True,blank=True)
#     competence4 = models.CharField(max_length=35,verbose_name='Compétence 4',null=True,blank=True)
#     competence5 = models.CharField(max_length=35,verbose_name='Compétence 5',null=True,blank=True)
#     competence6 = models.CharField(max_length=35,verbose_name='Compétence 6',null=True,blank=True)
#     image = models.ImageField(upload_to="media",error_messages="Seule les images sont autorisées",null=True,blank=True)


# class Profiles(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
#     Telephone = PhoneNumberField(max_length=14,null=True,blank=True, unique=True)
#     Fonctions = models.CharField(max_length=45,null=True,blank=True)
#     Experience = models.IntegerField(null=True,blank=True)
#     competence1 = models.CharField(max_length=35,verbose_name='Compétence 1',null=True,blank=True)
#     competence2 = models.CharField(max_length=35,verbose_name='Compétence 2',null=True,blank=True)
#     competence3 = models.CharField(max_length=35,verbose_name='Compétence 3',null=True,blank=True)
#     competence4 = models.CharField(max_length=35,verbose_name='Compétence 4',null=True,blank=True)
#     competence5 = models.CharField(max_length=35,verbose_name='Compétence 5',null=True,blank=True)
#     competence6 = models.CharField(max_length=35,verbose_name='Compétence 6',null=True,blank=True)
#     image = models.ImageField(upload_to="media/",error_messages="Seule les images sont autorisées",null=True,blank=True)

#     def __str__(self) -> str:
#         return self.Fonctions

#     class Meta:
        
#         verbose_name = 'Profil'
#         verbose_name_plural = 'Profiles'




