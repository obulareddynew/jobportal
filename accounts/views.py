from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        useremail=request.POST['inputEmail']
        password1=request.POST['firstpassword']
        password2 = request.POST['secondpassword']
        if password1==password2:
            if User.objects.filter(email=useremail).exists():
                messages.info(request,'Email Already Taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password1,email=useremail)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect('register')
    else:
        return render(request,'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['firstpassword']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')