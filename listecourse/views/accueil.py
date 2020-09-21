from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from listecourse.models import Liste, Produit
from django.urls import reverse


@login_required
def index(request):
    user = request.user
    context = {'liste': Liste.objects.filter(utilisateur=user)}
    return render(request, 'listecourse/accueil.html', context)


@login_required
def deleteProduit(request, nom_produit):
    user = request.user
    produit = Produit.objects.get(nomProduit=nom_produit)
    Liste.delete(Liste.objects.get(utilisateur=user, produit=produit))
    return HttpResponseRedirect(reverse('accueil'))


@login_required
def moreQuantite(resquest, nom_produit):
    user = resquest.user
    produit = Produit.objects.get(nomProduit=nom_produit)
    liste = Liste.objects.get(utilisateur=user, produit=produit)
    liste.quantite = liste.quantite + 1
    liste.save()
    return HttpResponseRedirect(reverse('accueil'))


@login_required
def lessQuantite(resquest, nom_produit):
    user = resquest.user
    produit = Produit.objects.get(nomProduit=nom_produit)
    liste = Liste.objects.get(utilisateur=user, produit=produit)
    if liste.quantite == 1:
        Liste.delete(liste)
    else:
        liste.quantite = liste.quantite - 1
        liste.save()
    return HttpResponseRedirect(reverse('accueil'))
