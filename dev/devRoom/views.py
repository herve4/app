from django.dispatch import receiver
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse

from devRoom.models import *
from devRoom.forms import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.core.validators import RegexValidator

from django.template import loader

def home(request):
    template = loader.get_template('home.html')
    
    # q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    # topics = theme.objects.all()
    # filters = theme.objects.filter(Q(room__theme__name__icontains=q))

    # if request.user.is_authenticated:
    #     user=request.user
    #     rooms = Room.objects.all().filter(
    #         Q(theme__name__icontains=q)|
    #         Q(name__icontains=q)|
    #         Q(description__icontains=q)|
    #         Q(host__username__icontains=q)
    #         )
    #     page = Paginator(rooms,6)
    #     page_list = request.GET.get('page')
    #     page = page.get_page(page_list)
        
    #     InstanceUserInfo = Profiles.objects.get(user=request.user)
    #     if InstanceUserInfo is None:
    #             redirect('profile', id=request.user.id)
    #     else:
    #         redirect('home')
    #     count_room = user.room_set.all().count()
    #     UserCount = User.objects.count()
    #     msg = Commentaires.objects.all().filter(user=request.user)
    #     participantss = request.user.participants_set.all().count()
    #     themeCount = request.user.theme_set.count()
    #     conversation = request.user.commentaires_set.all().count()
    #     context = {
    #             'themeCount':themeCount,
    #             'msg':msg,
    #             'InstanceUserInfo':InstanceUserInfo,
    #             'count_room':count_room,
    #             'UserCount':UserCount,
    #             'conversation':conversation,
    #             'participantss':participantss,
    #             'rooms':page,
    #             'count_room':count_room,
    #             'msg':filters,'q':q,
    #             'topics':topics
    #             }
    #     return render(request,'devRoom/home.html',context)
        
    # else:
    #     rooms = Room.objects.all().filter(
    #         Q(theme__name__icontains=q)|
    #         Q(name__icontains=q)|
    #         Q(description__icontains=q)|
    #         Q(host__username__icontains=q))
        
    #     page = Paginator(rooms,6)
    #     page_list = request.GET.get('page')
    #     page = page.get_page(page_list)
    #     count_room = rooms.count()
    #     context = {  
    #             'count_room':count_room,
    #             'rooms':page,
    #             'msg':filters,'q':q,
    #             'topics':topics,
    #             }
        
    context = {}   
    return HttpResponse(template.render(context,request))


# def profile(request, pk):
#     user = User.objects.get(id=pk)
#     rooms = user.room_set.all()
#     # imageU = Images.objects.get(id=pk)
#     UserForm = RegisterForm(instance=user)
#     room_message = user.commentaires_set.all()
#     InstanceUser = user.images_set.all()
#     InstanceUserInfo = Profiles.objects.get(user=request.user)
#     # InfoUsers = todoUserProfile.objects.get(id=pk)
#     InfoUserTodoForm = TodoUserForm(instance=InstanceUserInfo)
#     # formImage = ImageForm(instance=InstanceUserInfo)
#     themes = user.theme_set.all()
#     if request.method == 'POST':
#         # formImage = ImageForm(request.POST, instance=user)
#         InfoUserTodoForm = TodoUserForm(request.POST, request.FILES, instance=InstanceUserInfo)
#         UserForm = RegisterForm(request.POST, instance=user)
#         # if formImage.is_valid():
#         #     ImgForm = formImage.save(commit=False)
#         #     ImgForm.user = request.user
#         #     ImgForm.save()
#         if InfoUserTodoForm.is_valid():
#             InfoForm = InfoUserTodoForm.save(commit=False)
#             InfoForm.user = request.user
#             InfoForm.save()
#             if UserForm.is_valid():
#                 UserForm.save(commit=False)
#     # Images.objects.get_or_create(
#     #     fileUser=request.POST.get('img'),
#     #     user=user,  
#     # )
#     # info = todoUserProfile.objects.update(
        
#     #     Telephone=request.POST.get('phone'),
#     #     fonction=request.POST.get('fonction'),
#     #     Experience=request.POST.get('exp'),
#     #     competence1=request.POST.get('com1'),
#     #     competence2=request.POST.get('com2'),
#     #     competence3=request.POST.get('com3'),
#     #     competence4=request.POST.get('com4'),
#     #     image=request.POST['img']
#     # )
#         else:
#             context = {'UserForm':UserForm,'InfoUserTodoForm':InfoUserTodoForm,'user':user,'rooms':rooms,'msg':room_message,'topics':themes}
#             messages.error(request,'Données non insérées')
#             return render(request,'devRoom/profile.html',context)
#         # User.objects.update_or_create(username=request.POST.get('username'),email=request.POST.get('email'))
#         # else:
#         #     context = {'InfoUserTodoForm':InfoUserTodoForm,'user':user,'rooms':rooms,'msg':room_message,'topics':themes,'formImage':formImage}
#         #     messages.error(request,'Image non insérée')
#         #     return render(request,'devRoom/profile.html',context)
#         context = {'UserForm':UserForm,'InfoUserTodoForm':InfoUserTodoForm,'user':user,'rooms':rooms,'msg':room_message,'topics':themes}
#         return render(request,'devRoom/profile.html',context)
#     context = {'UserForm':UserForm,'InfoUserTodoForm':InfoUserTodoForm,'user':user,'rooms':rooms,'msg':room_message,'topics':themes}
#     return render(request,'devRoom/profile.html',context)

# def room(request,pk,*args,**kwargs):
#     page = 'room'
#     # room = None
#     # for i in rooms:
#     #     if i['Room'] == room_id:
#     #         room = i
#     # user = User.objects.get(id=pk)

#     room = Room.objects.get(id=pk)
    
    
   
#     counts = room.commentaires_set.all().count()
#     message =  room.commentaires_set.all()
#     participants = room.participants.all()

#     # rooms = user.room_set.all()
 

#     context = {'room':room,
               
#                'participants':participants,
                
#                 'message':message,
#                 'counts':counts,
#                 'page':page,
#                 'room':room
             
#                }
#     return render(request,'devRoom/room.html',context,*args)


# def room_one(request,room_id,*args,**kwargs):
#     page= 'room_one'
#     user = User.objects.get(id=room_id)
   
    
    
#     # RoomName = Room.objects.get(name=room_slug)
    
#     room=Room.objects.get(id=room_id)
#     form = CommentForm()
#     # RoomName2 = Room.objects.get(id=room_id)
#     messagess =  room.commentaires_set.all()
#     counts = room.commentaires_set.all().count()
#     participants = room.participants.all()
    

#     context = {
#             'page':page,
#             'messagess':messagess,
#             'room':room,
#             'counts':counts,
#             'participants':participants,
#             'form':form,
#             'user':user,
            
#             }  
    
#     if request.user.is_authenticated:
#         InstanceUserInfo = Profiles.objects.get(user=request.user)
#         context = {
#             'page':page,
#             'messagess':messagess,
#             'room':room,
#             'counts':counts,
#             'participants':participants,
#             'form':form,
#             'user':user,
#             'InstanceUserInfo':InstanceUserInfo,
#             } 
#         return render(request,'devRoom/room_one.html',context)
    
#     if request.method == 'POST' :
        
#         if request.user.is_authenticated:
            
#             # roomComment= Commentaires.objects.create(
#             #     user=user,
#             #     room=RoomName,
#             #     body=request.POST.get('msg'),
#             #     theme=RoomName.theme
#             #     )
            
#             # roomComment.save()
#             form = CommentForm(request.POST)
#             if form.is_valid():
                
#                 r = form.save(commit=False)
#                 r.host = request.user
#                 r.save()
                
#                 room.participants.add(request.user)
#                 # redirect('room_one',room_id=room.id)
#         else:
#             messages.error(request,"Veuillez vous connecter pour envoyer un commentaire !")
#             return render(request,'devRoom/room_one.html',context)
    
   
#     return render(request,'devRoom/room_one.html',context)


# # def ImageUserSideBar(request,instance):
# #      rooms = Room.objects.get(instance=room)
# #      one = Images.objects.all()
# #      UserImageSiderBar = [one.fileUser for ones in Images.objects.filter(room=rooms)]
# #      context = {'UserImageSiderBar':UserImageSiderBar}
# #      print(one['fileUser'])
# #      return render(request,'navbar.html',context)

# def search(request,room_id,*args,**kwargs):
#     user = User.objects.get(id=room_id)

#     room = Room.objects.get(id=room_id)
#     user2 = request.user
#     counts = room.commentaires_set.all().count()
#     message =  room.commentaires_set.all()
#     participants = room.participants.all()

#     rooms = user.room_set.all()
      
#     m= request.GET.get('m') if request.GET.get('m') != None else ''
#     t= request.GET.get('t') if request.GET.get('t') != None else ''
#     messageRoom =  room.commentaires_set.all().filter(
#     Q(body__icontains=m)|
#     Q(room__host__username__icontains=m)|
#     Q(room__name__icontains=m)                                     
#     ).order_by('-creat')
#     titre = Room.objects.filter(
#     Q(name__icontains=t)|
#     Q(theme__name__icontains=t)|
#     Q(description__icontains=t)                                   
#     ).order_by('-created')
    
#     if messageRoom is not None:
#         if counts >= 2:
#             messages.error(request,f'{counts} résultats trouvés') 
#             return render(request,'devRoom/room.html')
#         elif counts == 1:
#             messages.error(request,f'{counts} résultat trouvé')
#             return render(request,'devRoom/room.html')
#         else:
#             messages.error(request,f'{counts} résultat trouvé')
#             return render(request,'devRoom/room.html')
#     context = {'messageRoom':messageRoom,
#                'user':user,
#                'counts':counts,
#                'rooms':rooms,
#                't':t,
#                'user2':user2,
#                'titre':titre,
#                'participants':participants,
#                'message':message,
#                }
    
#     return render(request,'devRoom/room.html',context)



# @login_required(login_url='login_room')
# def room_creat(request,pk):
#     page = 'room_creat'
#     user = User.objects.get(id=pk)
#     themeall = user.theme_set.all()
#     roomAll = user.room_set.all()
#     # form = roomForm(instance=user)
#     if request.method == 'POST':
#         room = Room.objects.get(id=pk)
#         # form = roomForm(request.POST)
#         # print(request.POST)
#         theme_name = request.POST.get('theme')
#         if theme.objects.get(name=room.theme.name) == theme_name:
#             titre, created = theme.objects.update(user=request.user,name=theme_name)
#             insert= Room.objects.create(
#                 host=user,
#                 theme=titre,
#                 name=request.POST.get('titre'),
#                 description=request.POST.get('text')
#             )
#             insert.save()
#             return redirect('home')

#         else:
#             titre, created = theme.objects.get_or_create(user=user,name=theme_name)
#             insert= Room.objects.create(
#                 host=user,
#                 theme=titre,
#                 name=request.POST.get('titre'),
#                 description=request.POST.get('text')
#             )
#             insert.save()
#             return redirect('home')
#         # if form.is_valid():
            
#         #     room = form.save(commit=False)
#         #     room.host = request.user
#         #     room.save()
         
    
#     return render(request,'devRoom/room_form.html',{'themeall':themeall,'roomAll':roomAll,'page':page})
# @login_required(login_url='login_room')
# def updateRoom(request, pk):
#     page = 'updateRoom'
#     # user = User.objects.get(id=pk)
#     room = Room.objects.get(pk=pk)
#     form = roomForm(instance=room)
#     recup = room.theme
#     if request.user != room.host:
#         return HttpResponse('Vous n y\'êtes pas autorisé !')
#     if request.method == 'POST':
#         form = roomForm(request.POST, instance=room)
#         # theme_name = request.POST.get('theme')
#         # titre= theme.objects.update(user=request.user,name=theme_name)
#         # Room.objects.update(
#         #     host=request.user,
#         #     theme=titre,
#         #     name=request.POST.get('titre'),
#         #     description=request.POST.get('text')
#         # )
#         if form.is_valid():
#             form.save()
    
#         return redirect('home')
#     form = roomForm(instance=room)
#     context = {'form':form,'room':room,'page':page,'recup':recup}
#     return render(request,'devRoom/room_form.html',context)
# @login_required(login_url='login_room')
# def deleteRoom(request, pk):
#     page = 'deleteRoom'
#     room = Room.objects.get(id=pk)
#     if request.user != room.host:
#         return HttpResponse('Vous n y\'êtes pas autorisé !')
#     if request.method == 'POST':
#         room.delete()
#         return redirect('home')
#     return render(request,'devRoom/home.html',{'t':room,'page':page})


# def login_room(request):
#     page = 'login_room'
#     if request.user.is_authenticated:
#         return redirect('home')
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         pwd = request.POST.get('password')

#         try:
#             user = User.objects.get(username=username)
#             user = authenticate(request,username = user.username, password=pwd)
#             if user is not None:
#                 login(request,user)
#                 return redirect('home')
#         except:
#             messages.error(request,'Utilisateur ou mot de passe incorrect !')

#         else:
#             msg = "erreur d'authentification !"
#             messages.error(request,msg.capitalize())
            
#     context = {'page':page}
#     return render(request,'devRoom/login_room.html',context)

# def password_reset(request):
    
#     context = {}
#     return render(request,'devRoom/registration/password_reset_form.html',context)

# def register_room(request):
#     page = 'register_room'
    
#     formRegister = RegisterForm()
#     InfoUserTodoForm = TodoUserForm()
#     if request.method == 'POST':
#         formRegister = RegisterForm(request.POST)
        
#         # InfoUsers = todoUserProfile.objects.get(id=pk)
#         # InfoUserTodoForm = TodoUserForm(request.POST)
        
#         if formRegister.is_valid():
#             # if phone is not None:
               
#             #     # UserFro = UserFrom.save(commit=False)

#             #     user = formRegister.save(commit=False)
#             #     user.username = user.username.capitalize()
#             #     user.save()

#             #     FormUser = todoUserProfile.objects.create(Telephone=phone)
#             #     FormUser.save()
#             #     print(user)
#             #     if FormUser.Telephone == phone:
#             #         messages.error(request,"Cet ID existe déjà !")
#             #         return redirect('register_room')
#             #     else:
                    
#             #         login(request,user)
#             #         return redirect('home')
#             # else:
#             #     messages.error(request,'Erreur du champ contact !')
#                 verify_Email = User.objects.filter(email=formRegister.instance.email)
#                 if verify_Email.count():
#                     messages.error(request,'Cet email existe déjà !')
#                 else:
#                     user = formRegister.save(commit=False)
#                     user.username = user.username.capitalize()
#                     user.save()

                    
                   
#                     # f = InfoUserTodoForm.save(commit=False)
#                     # f.user = user
#                     # f.save()
#                     return redirect('login_room')
#         else:
#          messages.error(request,'Une erreur est survenue lors de l\'inscription')
    
#     context = {'formRegister':formRegister,'page':page,'InfoUserTodoForm':InfoUserTodoForm}
#     return render(request,'devRoom/login_room.html',context)

# def logoutUser(request):
#     logout(request)
#     return redirect('login_room')


# @login_required(login_url='login_room')
# def deleteMessage(request, pk):
#     deleteMessage = Commentaires.objects.get(id=pk)
#     if request.user != deleteMessage.user:
#         return HttpResponse('Vous n y\'êtes pas autorisé !')
#     if request.method == 'POST':
#         deleteMessage.delete()
#         redirect('home')
#     return render(request,'devRoom/deleteRoom.html',{'t':deleteMessage})
# # @receiver(sender=room)
# def UserProfile(request,user_id):
#     user = User.objects.get(id=user_id)
#     # user = User.objects.get(id=user_id)
#     room = Room.objects.get(id=user_id)
#     messagess = user.room_set.all()
#     participant = room.participants.all()
#     sujets = Room.objects.all().filter(host=room.id)
#     # sujet = slice(sujets,4)
    
#     commmentaires = room.usermessage_set.all()
#     topics = user.theme_set.all()
#     infos = user.profiles_set.all()
#     if request.method =='POST':      
#         if request.user.is_authenticated:
#             UserMessage.objects.get_or_create(
#             name=request.POST.get('com'),
#             user=request.user,
#             room = room,
#             theme = room.theme
#             )
                    
#             redirect('UserProfile',user_id=user.id)
#         else:
#             return HttpResponse('Veuillez vous connecter d\'abord !')

#     userCurrent = request.user.is_authenticated
#     if userCurrent:
#         UserCount = User.objects.count()
#         InstanceUserInfo = Profiles.objects.get(user=request.user)
#         participantss = request.user.participants_set.all().count()
#         themeCount = request.user.theme_set.count()
#         conversation = request.user.commentaires_set.all().count()

#         context = { 'participant':participant,
#                     'messages':messagess,
#                     'user':user,
#                     'infos':infos,
#                     'sujets':sujets,
#                     'themeCount':themeCount,
#                     'InstanceUserInfo':InstanceUserInfo,
#                     'UserCount':UserCount,
#                     'conversation':conversation,
#                     'participantss':participantss,
#                     'commmentaires':commmentaires,
#                     'topics':topics,  
#                 }
#         return render(request,'devRoom/profile_one_show.html',context,status=202)
    

       
#     context = { 'participant':participant,
#                 'messages':messagess,
#                 'user':user,
#                 'sujets':sujets,
#                 'infos':infos,
#                 'commmentaires':commmentaires,
#                 'topics':topics,  
#             }
#     return render(request,'devRoom/profile_one_show.html',context,status=202)

# def profilShow(request):
#     if request.user.is_authenticated:
       
#         InstanceUserInfo = Profiles.objects.get(user=request.user)
#         return render(request,'main.html',{'InstanceUserInfo':InstanceUserInfo})
    

