from django.shortcuts import render
from .models import *
from .forms import *
from account.models import User

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


def consulterFraisView(request, id):
    idFiche = FicheFrais.objects.get(idFicheFrais=id)
    #matriculeFiche = idFiche.objects.get(matricule)
    #print(matriculeFiche)
    #idUser = idFiche.objects.get(matricule)

    context = {
        'fiche':idFiche,
    }
    return render(request, 'fichefrais/consulter-frais.html', context)
