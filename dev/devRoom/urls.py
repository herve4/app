from django.conf import settings
from django.urls import include, path
from . import views

from django.conf.urls.static import static


urlpatterns = [
    # path('login/',views.login_room,name='login_room'),
   
    # path('login/reset-password/',views.password_reset,name='password_reset'),
    # path('register/',views.register_room,name='register_room'),
    # path('logout/',views.logoutUser,name='logout'),
    # path('',views.home,name='home'),
    # path('profile-user/<int:user_id>/',views.UserProfile,name='UserProfile'),
    # # path('mode_blog/',views.sett_view_room,name='sett_view_room'),
    # path('<int:pk>/creer-sujet/',views.room_creat,name='room_creat'),
    # path('Update-sujet/?q=<int:pk>/',views.updateRoom,name='updateRoom'),
    # path('Delete-sujet/?q=<int:pk>/',views.deleteRoom,name='deleteRoom'),
    # path('delete-message/?q=<int:pk>/',views.deleteMessage,name='deleteMessage'),
    # path('room/<str:pk>/',views.room,name='room'),
    # path('room_one/<str:room_id>/',views.room_one,name='room_one'),
    # path('room/<int:room_id>/search/',views.search,name='search'),
    # path('profile/<str:pk>/',views.profile,name='profile'),

]+ static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
