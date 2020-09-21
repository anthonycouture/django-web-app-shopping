from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms


def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('accueil'))
            else:
                return HttpResponseRedirect(reverse('login'))
    else:
        form = LoginForm()

    return render(request, 'listecourse/login.html', {'form': form})


class LoginForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisateur', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), label='Mot de passe')
