from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from .forms import BlogForm
from .models import blogs

def home(request):
    return render(request,'blog/home.html')

def current(request):
    return render(request, 'blog/current.html')

def signupuser(request):
   if request.method == 'GET':
        return render(request, 'blog/signupuser.html', {'form': UserCreationForm()})
   else:
       if request.POST['password1'] == request.POST['password2']:
           try:
               user=User.objects.create_user(request.POST['username'], password=request.POST['password1'])
               user.save()
               login(request, user)
               return redirect('current')
           except IntegrityError:
               return render(request, 'blog/signupuser.html', {'form': UserCreationForm(), 'error':'Username is alreay taken choose another'})

       else:
           return render(request, 'blog/signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords did not matched'})


def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'blog/loginuser.html', {'form': AuthenticationForm()})
    else:
        user=authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'blog/loginuser.html', {'form': AuthenticationForm(),'error':'Username and password did not matched'})
        else:
            login(request, user)
            return redirect('current')
def createblog(request):
    context={}
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            tittle = form.cleaned_data.get("tittle")
            image = form.cleaned_data.get("image")
            author=form.cleaned_data.get("url")
            url=form.cleaned_data.get("url")
            description=form.cleaned_data.get("description")
            obj = blogs.objects.create(
                title=tittle,
                image=image,
                #author=author,
                url=url,
                description=description,
            )
            obj.save()
            print(obj)
    else:
        form = BlogForm()
    context['form']=BlogForm()
    return render(request,'blog/createblog.html',context)