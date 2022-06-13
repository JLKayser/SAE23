from django.db import models

#____________________________________________________________
class cat_product(models.Model):
    nom = models.CharField(max_length=100)
    descriptif = models.CharField(max_length=100)

    def __str__(self):
        chaine = f"{self.nom} ({self.descriptif})"
        return chaine

    def dictionnaire(self):
        return {"nom":self.nom,"descriptif":self.descriptif}

#____________________________________________________________
class product(models.Model):
    produit = models.CharField(max_length=100)
    date = models.DateField()
    photo = models.URLField(null=True, blank=True)
    marques = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    categorie = models.ForeignKey("cat_product",on_delete=models.CASCADE, null=True)

    def __str__(self):
        chaine = f"{self.produit} | {self.categorie}"
        return chaine

    def dictionnaire(self):
        return {"produit":self.produit, "date":self.date,"photo":self.photo,"marques":self.marques,"auteur":self.auteur,"categorie":self.categorie}


#____________________________________________________________
class client(models.Model):
    num_client = models.BigIntegerField(null=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_inscription = models.DateField()
    adresse = models.CharField(max_length=100)

    def __str__(self):
        chaine = f"{self.nom} {self.prenom} (n°{self.num_client})"
        return chaine

    def dictionnaire(self):
        return {"num_client":self.num_client,"nom":self.nom,"prenom":self.prenom,"date_inscription":self.date_inscription,"adresse":self.adresse}


#____________________________________________________________
class commandes(models.Model):
    num_commande = models.BigIntegerField(null=True)
    client = models.ForeignKey("client",on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        chaine = f"{self.num_commande} | {self.client}"
        return chaine

    def dictionnaire(self):
        return {"num_commande":self.num_commande,"client":self.client,"date":self.date}


#____________________________________________________________
class liste_produit(models.Model):
    produit = models.ManyToManyField("product", blank=True)
    quantite = models.BigIntegerField()

    def __str__(self):
        chaine = f"{self.produit} | {self.quantite}"
        return chaine

    def dictionnaire(self):
        return {"produit":self.produit,"quantite":self.quantite}

#____________________________________________________________
class liste_commande(models.Model):
    commande = models.ForeignKey("commandes",on_delete=models.CASCADE)
    produit = models.ForeignKey("liste_produit",on_delete=models.CASCADE)

    def __str__(self):
        chaine = f"{self.commande} | {self.produit}"
        return chaine

    def dictionnaire(self):
        return {"commande":self.commande,"produit":self.produit}