from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.contrib.auth.models import User


def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegistrationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            password2 = request.POST['password2']
            email = request.POST['email']
            if password == password2:
                user = User.objects.create_user(username, email, password)
                user.save()
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse('accueil'))
                else:
                    return HttpResponseRedirect(reverse('login'))
    else:
        form = RegistrationForm()

    return render(request, 'listecourse/registration.html', {'form': form})


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisateur', max_length=100)
    email = forms.EmailField(label='Adresse mail')
    password = forms.CharField(widget=forms.PasswordInput(), label='Mot de passe')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirmation du mot de passe')
