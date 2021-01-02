from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import *
from fichefrais.models import *


# Create your views here.
@login_required(login_url='login:login')
def suiviVisiteurView(request):
    return render(request, 'suivi/suivi-visiteur.html')



@login_required(login_url='login:login')
@staff_member_required
def suiviComptableView(request):
    fiche = FicheFrais.objects.all()    
    context = {
        'ficheAllArray':fiche
    }
    return render(request, 'suivi/suivi-comptable.html', context)
