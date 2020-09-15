from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from listecourse.models import Liste

@login_required
def index(request):
    user = request.user
    context = {'liste': Liste.objects.all().filter(utilisateur=user)}
    return render(request, 'listecourse/accueil.html', context)
