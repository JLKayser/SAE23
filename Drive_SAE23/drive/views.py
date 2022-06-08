from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import Categorie, Commande, Client, Produit
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
		return HttpResponseRedirect("/drive/index-catégorie/")
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