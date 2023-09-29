
from django.urls import reverse_lazy
from django.views.generic import View
from django.conf import settings
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout,get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm
from django.contrib.auth.views import LoginView
from . import forms
import requests
from world.forms import *
from django.db.models import Q
from django.core.paginator import Paginator


User = get_user_model()

def home(request):
    pages = 'home'
    template = loader.get_template('devRoom/home.html')
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    # user = User.objects.get(id=request.user)
    sujets = Sujets.objects.all()
     
    # s = request.user.sujets_set.all().filter(participants)
    filters = Sujets.objects.filter(Q(theme__icontains=q))
    

    if request.user.is_authenticated:
        user=request.user
        rooms = Sujets.objects.all().filter(
            Q(theme__icontains=q)|
            Q(name__icontains=q)|
            Q(description__icontains=q)
            
            )
        if rooms is None:
            # return HttpResponse("devRoom/room_form.html")
            redirect('room_creat',id=request.user.id)
        
        page = Paginator(rooms,4)
        page_list = request.GET.get('page')
        page = page.get_page(page_list)
        sujets = Sujets.objects.all().filter(user=request.user.id)
        if request.user == 'is_active':
            resp = 'On'
            return HttpResponse(template.render({'resp':resp}, request))
        
            

        # room_user = [img.image for u in Profiles.objects.all()[:1]]
        # url = 'http://127.0.0.1:8000/{}'.format(img.image)
 
        # r_f = requests.get(url)
        # print(r_f)
        # contents = bs(r_f.content, 'html.parser')
        # profile_img = contents.find('img',{'alt':'Avatar'})['src']
        
        # if request.user != Sujets.objects.all():
        #    redirect('room_creat',id=request.user.pk)
        # else:
        #     room = Sujets.objects.get(user=request.user)
        #     participantss = room.participate.all().count()
        #     context = {'participantss':participantss}
        #     return HttpResponse(template.render(context, request))
        comment = request.user.messagesuser_set.all().count()
        us = User.objects.get(email=request.user)
        themeCount = user.sujets_set.all().count()
        UserCount = User.objects.all().count()
        msg = Commentaires.objects.all().filter(user=request.user)
        
        
        commentaires = request.user.commentaires_set.all().count()
        context = {

                'themeCount':themeCount,
                'msg':msg,
                'pages':pages,
                'UserCount':UserCount,
                'commentaires':commentaires,
                'rooms':page,             
                'msg':filters,'q':q,
                'sujets':sujets,
                'user':user,
                'comment':comment
                }
        return HttpResponse(template.render(context, request))

    else:
        rooms = Sujets.objects.all().filter(
            Q(theme__icontains=q)|
            Q(name__icontains=q)|
            Q(description__icontains=q)|
            Q(user__email__icontains=q))
        
        page = Paginator(rooms,4)
        page_list = request.GET.get('page')
        page = page.get_page(page_list)
        
        context = {  
                
                'rooms':page,
                'msg':filters,'q':q,
                'sujets':sujets,
                'pages':pages,
                }
        return render(request,'devRoom/home.html',context)

class ProfilesUserCurrent(View):
    template_name = 'devRoom/profile_form.html'
    
    pages = 'profile'
    def get(self,req,pk, *args,**kwargs):
        user = User.objects.get(id=pk)
        form = ProfilForm(instance=user)
        pages = self.pages
        context = {'form':form,'pages':pages}
        return render(req,self.template_name,context,**kwargs)
    def post(self,req,pk ,*args,**kwargs):
        user = User.objects.get(id=pk)
        form = ProfilForm(req.POST, instance=user)
        try:
            if form.is_valid():
                form.save(commit=False)
            else:
                messages.error(req,"ERREUR !")
        except:
            messages.error(req,"ERREUR DE MODIFICATION")
        context = {'form':form,'pages':self.pages}
        return render(req,self.template_name,context,**kwargs)



def prof(req,pk):
    
    user = User.objects.get(id=pk)
    form = UserChangeForm(instance=req.user)
  
    if req.method == 'POST':
        form = UserChangeForm(req.POST, req.FILES)
        
        if form.is_valid():
                form.save(commit=False)
                
                
              
                messages.success(req,"Profil modifié avec succès")
                return redirect('home')
        else:
         messages.error(req,'Une erreur est survenue lors de l\'inscription')
    
    context = {'form':form}
    return render(req,'registration/t.html',context)

def register_room(req):
    pages = 'register_room'
   
    formRegister = UserAdminCreationForm()
  
    if req.method == 'POST':
        formRegister = UserAdminCreationForm(req.POST)
        
        if formRegister.is_valid():
                formRegister.save()
                messages.success(req,"Compte crée avec succès")
                return redirect(settings.ACCOUNT_LOGOUT_REDIRECT_URL)
        else:
         messages.error(req,'Une erreur est survenue lors de l\'inscription')
    
    context = {'formRegister':formRegister,'pages':pages}
    return render(req,'devRoom/login_room.html',context)

# class loginUserView(View):
#     template_name = 'registration/login.html'
#     form_class = loginForm()
#     def get(self, request):
#         form = loginForm()
#         context={'form':form}
#         return render(request, self.template_name,context)
    
#     def post(self, request):
#             form = loginForm(request.POST)
#             user = authenticate(email= self.clean_data.get('email'),password= self.clean_data.get('password'))
#             if form.is_valid():
                
#                 if user is not None:
#                     login(request, user)
#                     redirect('home')
#             else:
#                 context={'form':form}
#                 messages.error(request,'Identifiants invalid !')
#                 return render(request, self.template_name,context)
class MyLoginView(LoginView):
    redirect_authenticated_user = True
    def get_success_url(self) -> str:
        return reverse_lazy('home')
    def form_invalid(self, form: AuthenticationForm) -> HttpResponse:
        messages.error(self.request,"Email ou mot de passe invalid !")
        return self.render_to_response(self.get_context_data(form=form))
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs is None:
            raise forms.ValidationError("Email incorrect !")
        return email
    


def logoutUser(request):
    logout(request)
    return redirect(settings.ACCOUNT_LOGOUT_REDIRECT_URL)


@login_required(login_url=settings.ACCOUNT_LOGOUT_REDIRECT_URL)
def room_creat(request,pk):
    page = 'room_creat'
    # users = User.objects.get(id=pk)
    suj = User.objects.get(id=pk)
    SujetForms = SujetForm()
    
    if request.method == 'POST':
        SujetForms = SujetForm(request.POST, request.FILES)
        if SujetForms.is_valid():
            f = SujetForms.save(commit=False)
            f.user = request.user
            f.save()
            
            messages.success(request,"Sujet crée avec succès !")
            return redirect(settings.LOGIN_REDIRECT_URL)  
        else:
            messages.error(request,"Pas inséré !")
            return render(request,'devRoom/room_form.html',{'SujetForms':SujetForms,'page':page,})
    
    return render(request,'devRoom/room_form.html',{'SujetForms':SujetForms,'page':page})


@login_required(login_url=settings.ACCOUNT_LOGOUT_REDIRECT_URL)
def updateRoom(request, pk):
    page = 'updateRoom'
    # user = User.objects.get(id=pk)
    room = Sujets.objects.get(pk=pk)
    form = SujetForm(instance=room)
    recup = room.theme
    if request.user != room.user:
        return HttpResponse('Vous n y\'êtes pas autorisé !')
    if request.method == 'POST':
        form = SujetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
        return redirect('home')
    
    context = {'form':form,'room':room,'page':page,'recup':recup}
    return render(request,'devRoom/room_form.html',context)

@login_required(login_url=settings.ACCOUNT_LOGOUT_REDIRECT_URL)
def deleteRoom(request, pk):
    page = 'deleteRoom'
    room = Sujets.objects.get(id=pk)
    if request.user != room.user:
        return HttpResponse('Vous n y\'êtes pas autorisé !')
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request,'devRoom/home.html',{'t':room,'page':page})



def UserProfile(request,user_id):
    # user = User.objects.get(id=user_id)
    # user = User.objects.get(id=user_id)
    pages = 'UserProfile'
    user = Sujets.objects.get(id=user_id)
    user2 = User.objects.get(id=user.user.id)
    sujet_en_traiter = user.name
    SER = Sujets.objects.all().filter(theme=user.theme)
    
    parts = user.participate.all()
    sujets = user2.sujets_set.all()
    
    img = User.objects.all().filter(id=user.user.id)
    img2 = User.objects.get(id=user.user.id)
    conversations = MessagesUser.objects.all().filter(sujets=user)
    topics = user2.sujets_set.all()
    infos = User.objects.all().filter(id=user.user.id)
    if request.method =='POST':      
        if request.user.is_authenticated:
            MessagesUser.objects.get_or_create(
            body=request.POST.get('com'),
            user=request.user,
            sujets=user,
            )
            user.participate.add(request.user)
            user.save()      
            redirect('UserProfile',user_id=user.id)
        else:
            return HttpResponse('Veuillez vous connecter d\'abord !')

    userCurrent = request.user.is_authenticated
    if userCurrent:
        context = { 
                    'parts':parts,
                    'infos':infos,
                    'img2':img2,
                    'sujet_en_traiter':sujet_en_traiter,
                    'SER':SER,
                    'sujets':sujets,
                    'conversations':conversations,
                    'topics':topics,
                    'img':img, 
                    'user':user,
                    'pages':pages, 
                }
        return render(request,'devRoom/profile_one_show.html',context,status=202)
    

       
    context = { 
                'parts':parts,
                'sujets':sujets,
                'infos':infos,
                'sujet_en_traiter':sujet_en_traiter,
                'pages':pages,
                'conversations':conversations,
                'topics':topics,
                'user':user,
                'img2':img2,
                'SER':SER,   
            }
    return render(request,'devRoom/profile_one_show.html',context,status=202)





def room(request,pk,*args,**kwargs):
    pages = 'room'
    # room = None
    # for i in rooms:
    #     if i['Room'] == room_id:
    #         room = i
    # user = User.objects.get(id=pk)

    room = Sujets.objects.get(id=pk)
    
    
    
    counts = room.commentaires_set.all().count()
    message =  room.commentaires_set.all()
    participant = Sujets.objects.all().filter(name=room.user)

    # rooms = user.room_set.all()
 

    context = {'room':room,
               
               'participant':participant,
                'message':message,
                'counts':counts,
                'pages':pages,
                'room':room
             
               }
    return render(request,'devRoom/room.html',context,*args)

@login_required(login_url=settings.ACCOUNT_LOGOUT_REDIRECT_URL)
def room_one(request,room_id,*args,**kwargs):
    pages= 'room_one'
    user = Sujets.objects.get(id=room_id)
    user2 = User.objects.get(email=user.user)
    
    room = Sujets.objects.get(id=room_id)
    formComment = CommentForm()
    
    # RoomName2 = Room.objects.get(id=room_id)
    
    messagess =  Commentaires.objects.all().filter(sujets=user)
    counts = Commentaires.objects.all().filter(sujets=user).count()
    participantss = user.participate.all()
    countParticipant =  Commentaires.objects.all().filter(sujets=user).count()
    
    img = User.objects.all().filter(id=user.user.id)
    # img = [im.image for img in Profiles.objects.all()]
    # print(img)
  
    
    if request.method == 'POST' :
        
        Comment = request.POST.get('commment')
        formComment = CommentForm(request.POST)
        context = {
            'pages':pages,
            'messagess':messagess,
            'room':room,
            'counts':counts,
            'formComment':formComment,
            'user':user,
            'participantss':participantss,
            'img':img,
            'countParticipant':countParticipant,
            }
        if request.user.is_authenticated:

            s = Commentaires.objects.create(
                user=request.user,
                sujets = user,
                body = Comment,    
            )
            s.save()
            room.participate.add(request.user)
            likesSujets.objects.add
        else:
            messages.error(request,"Veuillez vous connecter pour envoyer un commentaire !")
            redirect('room_one',room_id=room.id)
    context = {
            
            'messagess':messagess,
            'room':room,
            'counts':counts,
            'formComment':formComment,
            'user':user,
            'participantss':participantss,
            'img':img,
            'pages':pages,
            'countParticipant':countParticipant,
            }
    
    return render(request,'devRoom/room_one.html',context)

class search(View):
    template_name = 'devRoom/home.html'
    def get(self, request):
        get = Sujets.objects.all()
        context = {'room':get}
        return render(request, self.template_name,context)
    def post(self, request):
        pass

