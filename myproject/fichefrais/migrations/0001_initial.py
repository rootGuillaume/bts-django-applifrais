# Generated by Django 2.2.16 on 2021-01-02 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Etat',
            fields=[
                ('id', models.CharField(choices=[('RB', 'RB'), ('CL', 'CL'), ('CR', 'CR'), ('VA', 'VA')], max_length=2, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='FicheFrais',
            fields=[
                ('idFicheFrais', models.AutoField(primary_key=True, serialize=False)),
                ('mois', models.CharField(choices=[('Janvier', 'Janvier'), ('Février', 'Février'), ('Mars', 'Mars'), ('Avril', 'Avril'), ('Mai', 'Mai'), ('Juin', 'Juin'), ('Juillet', 'Juillet'), ('Aout', 'Aout'), ('Septembre', 'Septembre'), ('Octobre', 'Octobre'), ('Novembre', 'Novembre'), ('Décembre', 'Décembre')], max_length=20)),
                ('justificatif', models.BooleanField(null=True)),
                ('montantValide', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('dateModif', models.DateField(null=True)),
                ('annee', models.CharField(max_length=4)),
                ('idEtat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fichefrais.Etat')),
                ('matricule', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FraisForfait',
            fields=[
                ('id', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=20, null=True)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LigneFraisHorsForfait',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mois', models.CharField(max_length=6)),
                ('libelle', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(null=True)),
                ('montant', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('idFicheFrais', models.ManyToManyField(to='fichefrais.FicheFrais')),
                ('matricule', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LigneFraisForfait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mois', models.CharField(max_length=6)),
                ('idFraisForfait', models.CharField(max_length=3)),
                ('quantite', models.DecimalField(decimal_places=0, default=0, max_digits=11)),
                ('idFicheFrais', models.ManyToManyField(to='fichefrais.FicheFrais')),
                ('matricule', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]