from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

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
		model = models.product
		fields = ('nom', 'date', 'photo', 'marques','auteur','categorie')
		labels = {
			'nom' : _('Nom'),
			'date' : _("Date Péremption (mois/jour/année)"),
			'photo' : _('Photo'),
			'marques' : _('Marques'),
			'auteur' : _('Auteur'),
			'catégorie' : _('Catégorie')
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
			'produit' : _("Produit de la Commande")
			}



class ListeCommande(ModelForm):
	class Meta:
		model = models.liste_commande
		fields = ('commande', 'produit', 'quantite')
		labels = {
			'commande' : _('Commandes'),
			'produit' : _("Produit à ajouter"),
			'quantite' : _("Quantité du Produit")
			}