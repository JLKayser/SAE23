from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    
    path('drive/formulaire-catégorie/', views.formulaire_cat),
    path('drive/traitement-catégorie/', views.traitement_cat),
    path('drive/index-catégorie/', views.index_cat),
    path('drive/affiche-catégorie/<int:id>/', views.affiche_cat),
    path('drive/delete-catégorie/<int:id>/', views.delete_cat),
    path('drive/update-catégorie/<int:id>/', views.update_cat),
    path('drive/updatetraitement-catégorie/<int:id>/', views.updatetraitement_cat),

    path('drive/formulaire-commande/', views.formulaire_commande),
    path('drive/traitement-commande/', views.traitement_commande),
    path('drive/index-commande/', views.index_commande),
    path('drive/affiche-commande/<int:id>/', views.affiche_commande),
    path('drive/delete-commande/<int:id>/', views.delete_commande),
    path('drive/update-commande/<int:id>/', views.update_commande),
    path('drive/updatetraitement-commande/<int:id>/', views.updatetraitement_commande),

    path('drive/formulaire-client/', views.formulaire_client),
    path('drive/traitement-client/', views.traitement_client),
    path('drive/index-client/', views.index_client),
    path('drive/affiche-client/<int:id>/', views.affiche_client),
    path('drive/delete-client/<int:id>/', views.delete_client),
    path('drive/update-client/<int:id>/', views.update_client),
    path('drive/updatetraitement-client/<int:id>/', views.updatetraitement_client),

    path('drive/formulaire-produit/', views.formulaire_produit),
    path('drive/traitement-produit/', views.traitement_produit),
    path('drive/index-produit/', views.index_produit),
    path('drive/affiche-produit/<int:id>/', views.affiche_produit),
    path('drive/delete-produit/<int:id>/', views.delete_produit),
    path('drive/update-produit/<int:id>/', views.update_produit),
    path('drive/updatetraitement-produit/<int:id>/', views.updatetraitement_produit),
    path('drive/file_text', views.file_text, name='file_text'),

    path('drive/formulaire-liste-produit/', views.formulaire_liste_produit),
    path('drive/traitement-liste-produit/', views.traitement_liste_produit),
    path('drive/index-liste-produit/', views.index_liste_produit),
    path('drive/affiche-liste-produit/<int:id>/', views.affiche_liste_produit),
    path('drive/delete-liste-produit/<int:id>/', views.delete_liste_produit),
    path('drive/update-liste-produit/<int:id>/', views.update_liste_produit),
    path('drive/updatetraitement-liste-produit/<int:id>/', views.updatetraitement_liste_produit)
]