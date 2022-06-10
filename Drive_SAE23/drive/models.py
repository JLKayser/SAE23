from django.db import models


#____________________________________________________________
class cat_product(models.Model):
    nom = models.CharField(max_length=100)
    descriptif = models.CharField(max_length=100)

    def __str__(self):
        chaine = f"{self.nom} | {self.descriptif}"
        return chaine

    def dictionnaire(self):
        return {"nom":self.nom,"descriptif":self.descriptif}

#____________________________________________________________
class product(models.Model):
    nom = models.CharField(max_length=100)
    date = models.DateField()
    photo = models.FileField(upload_to='', storage=None, null=True, blank=True, default="APLU")
    marques = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    categorie = models.ForeignKey("cat_product",on_delete=models.CASCADE, null=True)

    def __str__(self):
        chaine = f"{self.nom} | {self.date} | {self.photo} | {self.marques} | {self.auteur} | {self.categorie}"
        return chaine

    def dictionnaire(self):
        return {"nom":self.nom, "date":self.date,"photo":self.photo,"marques":self.marques,"auteur":self.auteur,"categorie":self.categorie}

#____________________________________________________________
class client(models.Model):
    num_client = models.BigIntegerField(null=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_inscription = models.DateField()
    adresse = models.CharField(max_length=100)

    def __str__(self):
        chaine = f"{self.num_client} | {self.nom} | {self.prenom} | {self.date_inscription} | {self.adresse}"
        return chaine

    def dictionnaire(self):
        return {"num_client":self.num_client,"nom":self.nom,"prenom":self.prenom,"date_inscription":self.date_inscription,"adresse":self.adresse}


#____________________________________________________________
class commandes(models.Model):
    num_commande = models.BigIntegerField(null=True)
    client = models.CharField(max_length=100)
    date_inscription = models.DateField()

    def __str__(self):
        chaine = f"{self.num_commande} | {self.client} | {self.date_inscription}"
        return chaine

    def dictionnaire(self):
        return {"num_commande":self.num_commande,"client":self.client,"date_inscription":self.date_inscription}



#pour le moment on a pas encore réfléchi si on a besoin de 5 formulaire