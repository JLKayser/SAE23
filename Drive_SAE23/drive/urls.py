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


]