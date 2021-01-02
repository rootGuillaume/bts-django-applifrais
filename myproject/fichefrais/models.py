from django.db import models
from account.models import User

# Table Frais Forfait
class FraisForfait(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    libelle = models.CharField(max_length=20, null=True)
    montant = models.DecimalField(max_digits=5, decimal_places=2, null=True)



# Table Fiche Frais
class Etat(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    libelle = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.id



# Table Fiche Frais
class FicheFrais(models.Model):
    CHOICE = (
    ('Janvier', 'Janvier'), ('Février', 'Février'), ('Mars', 'Mars'), ('Avril', 'Avril'),
    ('Mai', 'Mai'), ('Juin', 'Juin'), ('Juillet', 'Juillet'), ('Aout', 'Aout'),
    ('Septembre', 'Septembre'), ('Octobre', 'Octobre'), ('Novembre', 'Novembre'), ('Décembre', 'Décembre'),
    )

    idFicheFrais = models.AutoField(primary_key=True)
    matricule = models.ManyToManyField(User)
    mois = models.CharField(max_length=20, choices=CHOICE, null=False)
    justificatif = models.BooleanField(null=True)
    montantValide = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    dateModif = models.DateField(null=True)
    idEtat = models.ForeignKey(Etat, on_delete=models.CASCADE)
    annee = models.CharField(max_length=4, null=False)



# Table Ligne Frais Forfait
class LigneFraisForfait(models.Model):
    idFicheFrais = models.ManyToManyField(FicheFrais)
    matricule = models.ManyToManyField(User)
    mois = models.CharField(max_length=6, null=False)
    idFraisForfait = models.CharField(max_length=3, null=False)
    quantite = models.DecimalField(max_digits=11, decimal_places=0, default=0)



# Table Ligne Frais Hors Forfait
class LigneFraisHorsForfait(models.Model):
    idFicheFrais = models.ManyToManyField(FicheFrais)
    id = models.AutoField(primary_key=True, null=False)
    matricule = models.ManyToManyField(User)
    mois = models.CharField(max_length=6, null=False)
    libelle = models.CharField(max_length=100, null=True)
    date = models.DateField(null=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2, default=0)
