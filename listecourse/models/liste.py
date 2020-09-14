from django.contrib.auth.models import User
from django.db import models
from listecourse.models import Produit


class Liste (models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    quantite = models.IntegerField()

    class Meta:
        unique_together = (("produit", "utilisateur"),)