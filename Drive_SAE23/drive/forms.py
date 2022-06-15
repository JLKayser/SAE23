from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms

class Categorie(ModelForm):
    class Meta:
        model = models.cat_product
        fields = ('nom', 'descriptif')
        labels = {
            'nom' : _('Nom'),
            'descriptif' : _("Descriptif")
            }


class Produit(ModelForm):
    class Meta:
        model = models.produit
        fields = ('produit', 'date', 'photo', 'marques','auteur','categorie','stock','prix')
        labels = {
            'produit' : _('Nom'),
            'date' : _("Date Péremption (mois/jour/année)"),
            'photo' : _('Photo'),
            'marques' : _('Marques'),
            'auteur' : _('Auteur'),
            'catégorie' : _('Catégorie'),
            'stock' : _('Stock du produit'),
            "prix" : _("Prix à l'unité"),
            }

class Client(ModelForm):
    class Meta:
        model = models.client
        fields = ('num_client', 'nom', 'prenom', 'date_inscription','adresse')
        labels = {
            'num_client' : _('Numéro Client'),
            'nom' : _("Nom du Client"),
            'prenom' : _('Prénom du Client'),
            'date_inscription' : _("Date d'inscription (mois/jour/année)"),
            'adresse' : _("Adresse")
            }


class Commande(ModelForm):
    class Meta:
        model = models.commandes
        fields = ('num_commande', 'client', 'date')
        labels = {
            'num_commande' : _('Numéro de Commandes'),
            'client' : _("Client"),
            'date' : _("Date (mois/jour/année)"),
            }



class ListeProduit(ModelForm):
    class Meta:
        model = models.liste_pc
        fields = ('commande','produit','quantite')
        labels = {
            'commande' : _("Commande "),
            'produit' : _("Produit de la commande"),
            'quantite' : _("Quantité du produit")
            }