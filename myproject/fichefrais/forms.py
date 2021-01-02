from django.forms import ModelForm
from .models import *


class NouveauFraisForm(ModelForm):
    class Meta:
        model = FicheFrais
        fields = '__all__'



class LigneFraisForfaitForm(ModelForm):
    class Meta:
        model = LigneFraisForfait
        fields = '__all__'



class LigneFraisHorsForfaitForm(ModelForm):
    class Meta:
        model = LigneFraisHorsForfait
        fields = '__all__'
