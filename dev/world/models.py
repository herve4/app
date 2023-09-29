import filecmp
import random
from typing import Optional
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from django_resized import ResizedImageField

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser doit avoir is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser doit avoir is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(_('Utilisateur'), unique=True,max_length=20,blank=True,null=True)
    email = models.EmailField(_('Adresse Email'), unique=True,blank=True,null=True)
    Telephone = PhoneNumberField(max_length=14, null=True, blank=True, unique=True)
    fonction = models.CharField(max_length=60,null=True,blank=True)
    adresse = models.CharField(max_length=255,null=True,blank=True)
    Experience = models.PositiveIntegerField(null=True,blank=True)
    competence1 = models.CharField(max_length=35,verbose_name='Compétence 1',null=True,blank=True)
    competence2 = models.CharField(max_length=35,verbose_name='Compétence 2',null=True,blank=True)
    competence3 = models.CharField(max_length=35,verbose_name='Compétence 3',null=True,blank=True)
    competence4 = models.CharField(max_length=35,verbose_name='Compétence 4',null=True,blank=True)
    competence5 = models.CharField(max_length=35,verbose_name='Compétence 5',null=True,blank=True)
    competence6 = models.CharField(max_length=35,verbose_name='Compétence 6',null=True,blank=True)
    image = ResizedImageField(size= [270, 250], crop=['middle','center'] ,upload_to="media/",default='media/media/2.jpg',error_messages="Seule les images sont autorisées",null=True,blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # def get_full_name(self):
    #     # L'utilisateur est identifié par son adresse e-mail
    #     return self.email
    # def get_short_name(self):
    #     # L'utilisateur est identifié par son adresse e-mail
    #     return self.email
    
    # def __str__(self):
    #     return self.email
    def has_perm(self, perm: str, obj=None):
        return True
        
    def has_module_perms(self, app_label: str):
        return True

    objects = CustomUserManager()

    class Meta:
        verbose_name ='Utilisateur par email'
        verbose_name_plural = 'Utilisateurs par email'

class likesSujets(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Utilisateur',null=True)
    likes = models.BooleanField(null=True,blank=True)


class Sujets(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Utilisateur',null=True)
    theme = models.CharField(max_length=200,verbose_name='Thème')
    name = models.CharField(max_length=60,verbose_name='Titre')
    likes = models.ForeignKey(likesSujets,on_delete=models.CASCADE,verbose_name='Likes',null=True)
    description = models.TextField(verbose_name='Description',max_length=1000)
    participate = models.ManyToManyField(User,related_name='participate')
    
    image = ResizedImageField(size= [1920, 350], crop=['middle','center'],upload_to="img-titre",error_messages="Seule les images sont autorisées",blank=True,null=True)
    created = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.name
    class Meta:
        ordering = ['-created','-update']
        verbose_name ='Titre'
        verbose_name_plural = 'Titres'

    def get_absolute_url(self):
        return reverse("world:room_one", args={self.id})
    

class MessagesUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Utilisateur',null=True)
    sujets = models.ForeignKey(Sujets,on_delete=models.CASCADE,verbose_name='Sujets',null=True)
    body = models.TextField(max_length=1000,verbose_name='Message')
    creat = models.DateTimeField(auto_now=True)
    mod = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.body[0:50]
    class Meta:
        ordering = ['-creat','-mod']
        verbose_name ='Message'
        verbose_name_plural = 'Messages'

class Commentaires(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Utilisateur',null=True)
    sujets = models.ForeignKey(Sujets,on_delete=models.CASCADE,verbose_name='Sujets',null=True)
    body = models.TextField(max_length=1000,verbose_name='Message')
    creat = models.DateTimeField(auto_now=True)
    mod = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.body[0:50]
    class Meta:
        ordering = ['-creat','-mod']
        verbose_name ='Commentaire'
        verbose_name_plural = 'Commentaires'

