from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import User


def loginPage(request):
    if request.method == 'POST':
        national_id = request.POST.get('national_id')
        password = request.POST.get('password')

        user = authenticate(request, username=national_id, password=password)

        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'users/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home-page')


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        national_id = request.POST.get('national_id')
        opt = request.POST.get('opt')
        if opt:
            user = User.objects.create_testeruser(email=email, first_name=first_name, last_name=last_name,
                                                  address=address, password=password, phone=phone,
                                                  national_id=national_id,
                                                  )
        else:
            user = User.objects.create_Teacheruser(email=email, first_name=first_name, last_name=last_name,
                                                   address=address, password=password, phone=phone,
                                                   national_id=national_id,
                                                   )
        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            messages.add_message(request, messages.error, 'Please Review Your Data Failed To Register')
    context = {}
    return render(request, 'users/register.html', context)
