from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('queue')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()

        context = {'form':form}
        return render(request, 'account/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('queue')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('queue')
            else:
                messages.info(request, 'Usuário OU senha incorreto!')

        return render(request, 'account/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

# Create your views here.
