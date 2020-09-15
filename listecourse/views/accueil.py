from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def index(request):
    message = "Hello World !"
    context = {'message': message}
    return render(request, 'listecourse/accueil.html', context)
