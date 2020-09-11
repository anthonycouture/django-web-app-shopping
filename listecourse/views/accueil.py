from django.shortcuts import render


def index(request):
    message = "Hello World !"
    context = {'message': message}
    return render(request, 'listecourse/accueil.html', context)
