from django.db import models


#____________________________________________________________
class cat_product(models.Model):
    nom = models.CharField(max_length=100)
    descriptif = models.CharField(max_length=100)

    def __str__(self):
        chaine = f"Voici le nom du produit : {self.nom} \n Descriptif : {self.descriptif}"
        return chaine

    def dictionnaire(self):
        return {"nom":self.nom,"descriptif":self.descriptif}

#____________________________________________________________
class product(models.Model):
    nom = models.CharField(max_length=100)
    date = models.DateField()
    photo = models.FileField(upload_to='', storage=None)
    marques = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    categorie = models.ForeignKey("cat_product",on_delete=models.CASCADE, null=True)

    def __str__(self):
        chaine = f"{self.nom}"
        return chaine

    def dictionnaire(self):
        return {"nom":self.nom}

#____________________________________________________________
class client(models.Model):
    num_client = models.BigIntegerField(null=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_inscription = models.DateField()
    adresse = models.CharField(max_length=100)

    def __str__(self):
        chaine = f"{self.nom}"
        return chaine

    def dictionnaire(self):
        return {"nom":self.nom}


#____________________________________________________________
class commandes(models.Model):
    num_commande = models.BigIntegerField(null=True)
    client = models.CharField(max_length=100)
    date_inscription = models.DateField()

    def __str__(self):
        chaine = f"{self.num_commande}"
        return chaine

    def dictionnaire(self):
        return {"nom":self.num_commande}



#pour le moment on a pas encore réfléchi si on a besoin de 5 formulaire