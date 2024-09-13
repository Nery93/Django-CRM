from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def home(request):
    #Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "You have been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There was an error in your login, please try again!!")
            return redirect('home')
    else:    
        return render(request, 'home.html')


def logout_user(request):
    logout(request)
    messages.success("You have been logged Out...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully.')
            return redirect('home')  # Redireciona para a página inicial após o registro
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})