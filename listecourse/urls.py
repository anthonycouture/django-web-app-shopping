from django.urls import path

from .views import accueil, login, logout, registration, addProduct, addProductInList

urlpatterns = [
    path('', accueil.index, name='accueil'),
    path('accounts/login/', login.index, name='login'),
    path('logout', logout.index, name='logout'),
    path('registration', registration.index, name='registration'),
    path('addProduct', addProduct.index, name='addProduct'),
    path('addProductInList', addProductInList.index, name='addProductInList'),
    path('deleteProductList/<str:nom_produit>', accueil.deleteProduit, name='deleteProductList'),
    path('moreQuantite/<str:nom_produit>', accueil.moreQuantite, name='moreQuantite'),
    path('lessQuantite/<str:nom_produit>', accueil.lessQuantite, name='lessQuantite'),
]
