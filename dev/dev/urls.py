
from django.contrib import admin
from django.urls import include, path
from devRoom.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('world.urls')),
    # path('',include('django.contrib.auth.urls')),
    
    path('accounts/',include('allauth.urls')),
    path('dashbord/',include('devRoom.urls')),
    # path('social/',TemplateView.as_view(template_name='devRoom/login_room.html'),name='login_room')
    
   
]
