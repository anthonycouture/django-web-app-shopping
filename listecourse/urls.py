from django.urls import path

from listecourse.views import accueil

urlpatterns = [
    path('', accueil.index, name='accueil index'),
]
