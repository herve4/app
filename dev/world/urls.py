from django import views
from django.urls import path, include
from world.views import *
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView,PasswordChangeView,PasswordChangeDoneView

urlpatterns = [
    path('',views.home,name='home'),
    # path('login/',LoginView.as_view(template_name='registration/login.html',redirect_authenticated_user=True),name='login'),
    path('modifier-mot-de-passe/',PasswordChangeView.as_view(template_name='registration/changePassord.html',success_url='PasswordChangeComplete/'),name='PasswordChange'),
    path('mot-de-passe-changer/',PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),name='PasswordChangeComplete'),
    path('register/',register_room,name='register_room'),
    path('<int:pk>/creer-sujet/',room_creat,name='room_creat'),
    path('Update-sujet/?q=<int:pk>/',views.updateRoom,name='updateRoom'),
    path('Delete-sujet/?q=<int:pk>/',views.deleteRoom,name='deleteRoom'),
    # path('account/',include('django.contrib.auth.urls'),name='login_room'),
    path('login/',MyLoginView.as_view(), name='login'),
    path('room/<str:pk>/',views.room,name='room'),
    path('room_one/<str:room_id>/',views.room_one,name='room_one'),
    path('profile-user/<int:user_id>/',views.UserProfile,name='UserProfile'),
    path('profile/<str:pk>/',ProfilesUserCurrent.as_view(),name='profile'),
    path('prof/<str:pk>/',views.prof,name='prof'),
    path('logout/',logoutUser,name='logoutUser'),
] + static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
