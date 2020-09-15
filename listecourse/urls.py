from django.urls import path

from .views import accueil, login, logout, registration

urlpatterns = [
    path('', accueil.index, name='accueil'),
    path('accounts/login/', login.index, name='login'),
    path('logout', logout.index, name='logout'),
    path('registration', registration.index, name='registration')
]
