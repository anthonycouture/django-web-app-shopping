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
        form = addProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('accueil'))
    else:
        form = addProductForm()

    return render(request, 'listecourse/addProduct.html', {'form': form})


class addProductForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nomProduit', 'illustration']
