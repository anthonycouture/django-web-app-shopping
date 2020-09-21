from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from listecourse.models import Produit, Liste


data = []

@login_required
def index(request):
    user = request.user
    if request.method == 'POST':
        print(request.POST)
        form = addProductInListForm(user, request.POST)
        if form.is_valid():
            name_product = request.POST['name_product']
            produit = Produit.objects.get(nomProduit=name_product)
            liste = Liste(produit=produit, utilisateur=user, quantite=1)
            try:
                liste.save()
            except:
                context = {'form': form, 'message': 'Un problème est survenu !!!'}
                return render(request, 'listecourse/addProductInList.html', context)
            return HttpResponseRedirect(reverse('accueil'))
    else:
        form = addProductInListForm(user)
    return render(request, 'listecourse/addProductInList.html', {'form': form})


class addProductInListForm(forms.Form):
    def __init__(self,user,*args, **kwargs):
        super(addProductInListForm, self).__init__(*args, **kwargs)
        self.fields['name_product'] = forms.ModelChoiceField(queryset=Produit.objects.exclude(liste__utilisateur=user))
