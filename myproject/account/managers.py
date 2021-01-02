from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group


# CUSTOM || Function to raise error
def errorFieldEmpty(value, message):
    if not value:
        raise ValueError(message)


# CUSTOM || Class to overwrite Django User creation
class UserAdminCreationForm(BaseUserManager):

    # DJANGO || Function to create user | Function parameters = REQUIRED_FIELDS + USERNAME_FIELD
    def create_user(self, username, email, nom, prenom, adresse, cp, ville, dateEmbauche, password=None):
        errorFieldEmpty(username, 'Username manquant.')
        errorFieldEmpty(email, 'Email manquant.')
        errorFieldEmpty(nom, 'Nom manquant.')
        errorFieldEmpty(prenom, 'Prénom manquant.')
        errorFieldEmpty(adresse, 'Adresse manquante.')
        errorFieldEmpty(cp, 'Code Postal manquant.')
        errorFieldEmpty(ville, 'Ville manquante.')
        errorFieldEmpty(dateEmbauche, "Date d'embauche manquante.")

        user = self.model(
                username=username,
                email=email,
                nom=nom,
                prenom=prenom,
                adresse=adresse,
                cp=cp,
                ville=ville,
                dateEmbauche=dateEmbauche,
        )

        user.set_password(password)
        user.save(using=self._db)

        group = Group.objects.get(name='Visiteur')
        user.groups.add(group)

        return user

    # DJANGO || Function to create super user | Function parameters = REQUIRED_FIELDS + USERNAME_FIELD
    def create_superuser(self, username, email, nom, prenom, adresse, cp, ville, dateEmbauche, password):
        user = self.create_user(
                password=password,
                username=username,
                email=email,
                nom=nom,
                prenom=prenom,
                adresse=adresse,
                cp=cp,
                ville=ville,
                dateEmbauche=dateEmbauche,
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
