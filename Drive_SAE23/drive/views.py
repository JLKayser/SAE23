from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import Categorie, Commande, Client, Produit, ListeCommande,ListeProduit
from . import models

def index(request):
	return render(request, "index.html")


#________________________ Catégorie____________________________ 
def formulaire_cat(request):
	if request.method == "POST":
		form = Categorie(request)
		if form.is_valid():
			categorie = form.save()
			return render(request,"categorie/affiche_cat.html",{"categorie" : categorie})
		else:
			return render(request,"categorie/formulaire_cat.html",{"form_cat": form})
	else :
		form = Categorie()
		return render(request,"categorie/formulaire_cat.html",{"form_cat" : form})


def traitement_cat(request):
	form = Categorie(request.POST)
	if form.is_valid():
		categorie = form.save()
		categorie.save()
		return HttpResponseRedirect("/drive/index-catégorie/")
	else:
		return render(request,"categorie/formulaire_cat.html",{"categorie" : categorie})

def index_cat(request):
	liste = list(models.cat_product.objects.all())
	return render(request,"categorie/index_cat.html",{"listALL_categorie": liste})

def affiche_cat(request, id):
	categorie = models.cat_product.objects.get(pk=id)
	return render(request,'categorie/affiche_cat.html',{"categorie": categorie})


def update_cat(request, id):
	categorie = models.cat_product.objects.get(pk=id)
	form = Categorie(categorie.dictionnaire())
	return render(request,'categorie/formulaire_cat.html',{"form_cat": form, "id_cat":id})


def updatetraitement_cat(request, id):
	form = Categorie(request.POST)
	if form.is_valid():
		categorie = form.save(commit=False)
		categorie.id = id
		categorie.save()
		return HttpResponseRedirect(f"/drive/index-catégorie/")
	else:
		return render(request,"categorie/formulaire_cat.html",{"form_cat": form, "id_cat":id})

def delete_cat(request, id):
	categorie = models.cat_product.objects.get(pk=id)
	categorie.delete()
	return HttpResponseRedirect("/drive/index-catégorie/")








#________________________Commande____________________________ 
def formulaire_commande(request):
	if request.method == "POST":
		form = Commande(request)
		if form.is_valid():
			commande = form.save()
			return render(request,"commande/affiche_commande.html",{"commande" : commande})
		else:
			return render(request,"commande/formulaire_commande.html",{"form_commande": form})
	else :
		form = Commande()
		return render(request,"commande/formulaire_commande.html",{"form_commande" : form})


def traitement_commande(request):
	form = Commande(request.POST)
	if form.is_valid():
		commande = form.save()
		commande.save()
		return HttpResponseRedirect("/drive/index-commande/")
	else:
		return render(request,"commande/formulaire_commande.html",{"commande" : commande})

def index_commande(request):
	liste = list(models.commandes.objects.all())
	return render(request,"commande/index_commande.html",{"listALL_commande": liste})

def affiche_commande(request, id):
	commande = models.commandes.objects.get(pk=id)
	return render(request,'commande/affiche_commande.html',{"commande": commande})


def update_commande(request, id):
	commande = models.commandes.objects.get(pk=id)
	form = Commande(commande.dictionnaire())
	return render(request,'commande/formulaire_commande.html',{"form_commande": form, "id_commande":id})


def updatetraitement_commande(request, id):
	form = Commande(request.POST)
	if form.is_valid():
		commande = form.save(commit=False)
		commande.id = id
		commande.save()
		return HttpResponseRedirect(f"/drive/index-commande/")
	else:
		return render(request,"commande/formulaire_commande.html",{"form_commande": form, "id_commande":id})

def delete_commande(request, id):
	commande = models.commandes.objects.get(pk=id)
	commande.delete()
	return HttpResponseRedirect("/drive/index-commande/")





#________________________Client____________________________ 
def formulaire_client(request):
	if request.method == "POST":
		form = Client(request)
		if form.is_valid():
			client = form.save()
			return render(request,"client/affiche_client.html",{"client" : client})
		else:
			return render(request,"client/formulaire_client.html",{"form_client": form})
	else :
		form = Client()
		return render(request,"client/formulaire_client.html",{"form_client" : form})


def traitement_client(request):
	form = Client(request.POST)
	if form.is_valid():
		client = form.save()
		client.save()
		return HttpResponseRedirect("/drive/index-client/")
	else:
		return render(request,"client/formulaire_client.html",{"client" : client})

def index_client(request):
	liste = list(models.client.objects.all())
	return render(request,"client/index_client.html",{"listALL_client": liste})

def affiche_client(request, id):
	client = models.client.objects.get(pk=id)
	return render(request,'client/affiche_client.html',{"client": client})


def update_client(request, id):
	client = models.client.objects.get(pk=id)
	form = Client(client.dictionnaire())
	return render(request,'client/formulaire_client.html',{"form_client": form, "id_client":id})


def updatetraitement_client(request, id):
	form = Client(request.POST)
	if form.is_valid():
		client = form.save(commit=False)
		client.id = id
		client.save()
		return HttpResponseRedirect(f"/drive/index-client/")
	else:
		return render(request,"client/formulaire_client.html",{"form_client": form, "id_client":id})

def delete_client(request, id):
	client = models.client.objects.get(pk=id)
	client.delete()
	return HttpResponseRedirect("/drive/index-client/")





#________________________Produit____________________________ 
def formulaire_produit(request):
	if request.method == "POST":
		form = Produit(request)
		if form.is_valid():
			produit = form.save()
			return render(request,"produit/affiche_produit.html",{"produit" : produit})
		else:
			return render(request,"produit/formulaire_produit.html",{"form_produit": form})
	else :
		form = Produit()
		return render(request,"produit/formulaire_produit.html",{"form_produit" : form})


def traitement_produit(request):
	form = Produit(request.POST)
	if form.is_valid():
		produit = form.save()
		produit.save()
		return HttpResponseRedirect("/drive/index-produit/")
	else:
		return render(request,"produit/formulaire_produit.html",{"produit" : produit})

def index_produit(request):
	liste = list(models.product.objects.all())
	return render(request,"produit/index_produit.html",{"listALL_produit": liste})

def affiche_produit(request, id):
	produit = models.product.objects.get(pk=id)
	return render(request,'produit/affiche_produit.html',{"produit": produit})


def update_produit(request, id):
	produit = models.product.objects.get(pk=id)
	form = Produit(produit.dictionnaire())
	return render(request,'produit/formulaire_produit.html',{"form_produit": form, "id_produit":id})


def updatetraitement_produit(request, id):
	form = Produit(request.POST)
	if form.is_valid():
		produit = form.save(commit=False)
		produit.id = id
		produit.save()
		return HttpResponseRedirect(f"/drive/index-produit/")
	else:
		return render(request,"produit/formulaire_produit.html",{"form_produit": form, "id_produit":id})

def delete_produit(request, id):
	produit = models.product.objects.get(pk=id)
	produit.delete()
	return HttpResponseRedirect("/drive/index-produit/")




#________________________Liste Commande____________________________ 
def formulaire_liste_commande(request):
	if request.method == "POST":
		form = ListeCommande(request)
		if form.is_valid():
			liste_commande = form.save()
			return render(request,"liste-commande/affiche_lc.html",{"lc" : liste_commande})
		else:
			return render(request,"liste-commande/formulaire_lc.html",{"form_lc": form})
	else :
		form = ListeCommande()
		return render(request,"liste-commande/formulaire_lc.html",{"form_lc" : form})


def traitement_liste_commande(request):
	form = ListeCommande(request.POST)
	if form.is_valid():
		liste_commande = form.save()
		liste_commande.save()
		return HttpResponseRedirect("/drive/index-liste-commande/")
	else:
		return render(request,"liste-commande/formulaire_lc.html",{"lc" : liste_commande})

def index_liste_commande(request):
	liste = list(models.liste_commande.objects.all())
	return render(request,"liste-commande/index_lc.html",{"listALL_lc": liste})

def affiche_liste_commande(request, id):
	liste_commande = models.liste_commande.objects.get(pk=id)
	return render(request,'liste-commande/affiche_lc.html',{"lc": liste_commande})


def update_liste_commande(request, id):
	liste_commande = models.liste_commande.objects.get(pk=id)
	form = ListeCommande(liste_commande.dictionnaire())
	return render(request,'liste-commande/formulaire_lc.html',{"form_lc": form, "id_lc":id})


def updatetraitement_liste_commande(request, id):
	form = ListeCommande(request.POST)
	if form.is_valid():
		liste_commande = form.save(commit=False)
		liste_commande.id = id
		liste_commande.save()
		return HttpResponseRedirect(f"/drive/index-liste-commande/")
	else:
		return render(request,"liste-commande/formulaire_lc.html",{"form_lc": form, "id_lc":id})

def delete_liste_commande(request, id):
	liste_commande = models.liste_commande.objects.get(pk=id)
	liste_commande.delete()
	return HttpResponseRedirect("/drive/index-liste-commande/")




#________________________Liste Produit____________________________ 
def formulaire_liste_produit(request):
	if request.method == "POST":
		form = ListeProduit(request)
		if form.is_valid():
			liste_produit = form.save()
			return render(request,"liste-produit/affiche_lp.html",{"lp" : liste_produit})
		else:
			return render(request,"liste-produit/formulaire_lp.html",{"form_lp": form})
	else :
		form = ListeProduit()
		return render(request,"liste-produit/formulaire_lp.html",{"form_lp" : form})


def traitement_liste_produit(request):
	form = ListeProduit(request.POST)
	if form.is_valid():
		liste_produit = form.save()
		liste_produit.save()
		return HttpResponseRedirect("/drive/index-liste-produit/")
	else:
		return render(request,"liste-produit/formulaire_lp.html",{"lp" : liste_produit})

def index_liste_produit(request):
	liste = list(models.liste_produit.objects.all())
	return render(request,"liste-produit/index_lp.html",{"listALL_lp": liste})

def affiche_liste_produit(request, id):
	liste_produit = models.liste_produit.objects.get(pk=id)
	return render(request,'liste-produit/affiche_lp.html',{"lp": liste_produit})


def update_liste_produit(request, id):
	liste_produit = models.liste_produit.objects.get(pk=id)
	form = ListeProduit(liste_produit.dictionnaire())
	return render(request,'liste-produit/formulaire_lp.html',{"form_lp": form, "id_lp":id})


def updatetraitement_liste_produit(request, id):
	form = ListeProduit(request.POST)
	if form.is_valid():
		liste_produit = form.save(commit=False)
		liste_produit.id = id
		liste_produit.save()
		return HttpResponseRedirect(f"/drive/index-liste-produit/")
	else:
		return render(request,"liste-produit/formulaire_lp.html",{"form_lp": form, "id_lp":id})

def delete_liste_produit(request, id):
	liste_produit = models.liste_produit.objects.get(pk=id)
	liste_produit.delete()
	return HttpResponseRedirect("/drive/index-liste-produit/")