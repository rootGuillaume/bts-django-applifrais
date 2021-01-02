from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def nouveauFraisView(request):
    fraisArray = FraisForfait.objects.all()
    context = {
        'fiche_frais':NouveauFraisForm(),
        'frais_forfait':LigneFraisForfaitForm(),
        'frais_hors_forfait':LigneFraisHorsForfaitForm(),
        'fraisArray':fraisArray,
    }
    return render(request, 'fichefrais/nouveau-frais.html', context)


def consulterFraisView(request):
    fraisArray = FraisForfait.objects.all()
    context = {
        'fraisArray':fraisArray,
    }
    return render(request, 'fichefrais/consulter-frais.html', context)
