from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Function to return User login view
#def loginUserView(request):

#    return render(request, 'login/login-page.html')


# Function to login User
def loginUser(request):
    if request.user.is_authenticated:
        print("connecté")
        #return redirect('suivi:suivi')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                print('connecté')
                #return redirect('suivi:suivi')
            else:
                messages.warning(request, 'Matricule ou Mot de passe incorrect')

    return render(request, 'login/login-page.html')

# Function to logout User
def logoutUser(request):
    logout(request)
    return redirect('login:login')
