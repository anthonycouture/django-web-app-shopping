from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from listecourse.models import Produit

@login_required
def index(request):
    if request.method == 'POST':
        form = addProductForm(request.POST)
        if form.is_valid():
            name_product = request.POST['name_product']
            produit = Produit(nomProduit=name_product)
            produit.save()
            return HttpResponseRedirect(reverse('accueil'))
    else:
        form = addProductForm()

    return render(request, 'listecourse/addProduct.html', {'form': form})


class addProductForm(forms.Form):
    name_product = forms.CharField(label='Nom du produit', max_length=50)
