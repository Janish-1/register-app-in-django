from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)

def home(request):
    return redirect('login')

def registerpage(request):
    if request.method=='POST':
        if request.POST.get('username') and request.POST.get('email') and request.POST.get('dob') and request.POST.get('p1') and request.POST.get('p2'):
            saverecord=User()
            saverecord.username=request.POST.get('username')
            saverecord.email=request.POST.get('email')
            saverecord.dob=request.POST.get('dob')
            saverecord.p1=request.POST.get('p1')
            saverecord.p2=request.POST.get('p2')
            saverecord.secques=request.POST.get('secques')
            saverecord.save()
            messages.success(request,"New user Registration Details Saved Successfully...!")
            return render(request,'login.html')
    else:
        return render(request,'register.html')

# def registerPage(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         form = User()
#         if request.method == 'POST':
#             form = User(request.POST)
#             if form.is_valid():
#                 form.save()
#                 user = form.cleaned_data.get('username')
#                 messages.success(request, 'Account was created for ' + user)
#                 return redirect('login')
#         context = {'form': form}
#         return render(request, 'register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username,email=email,p1=password,dob=dob)

            if user is not None:
                print("User Exists")
                return render(request,'dashboard.html',{"name":username,"dob":dob})
            else:
                messages.info(request,'WrongID/Password')
                return redirect('home')
        except Exception as e:
            messages.info(request, 'Please check the fields')

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    return redirect('home')

def forgetpassword(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        secques = request.POST.get('secques')
        newpass = request.POST.get('newpass')
    try:
        user = User.objects.get(username=username,email=email,secques=secques)
        if user is not None:
            print("User Exists")
            resetpassword(email,secques,newpass)
            return render(request,'resetpassword.html')
        else:
            messages.info(request,'Wrong details')
    except Exception as e:
        messages.info(request,'Please check the details')
    return render(request,'forgetpassword.html')

def resetpassword(email,secques,newpass):
    user = User.objects.get(email=email,secques=secques)
    user.p1=newpass
    user.p2=newpass
    user.save()
    print("Password Updated")