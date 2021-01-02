from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . import decorators

# Function to return User login view
#def loginUserView(request):

#    return render(request, 'login/login-page.html')


# Function to login User
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('suivi:suivi-visiteur')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

#                if groupRequired('Visiteur'):
#                    return redirect('suivi:suivi-visiteur')
#                elif groupRequired('Comptable'):
#                    return redirect('suivi:suivi-comptable')
            else:
                messages.warning(request, 'Matricule ou Mot de passe incorrect')

    return render(request, 'login/login-page.html')

# Function to logout User
def logoutUser(request):
    logout(request)
    return redirect('login:login')
