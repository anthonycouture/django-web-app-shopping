from django.db import models


class Utilisateur(models.Model):
    email = models.CharField(primary_key=True, max_length=255)
    mdp = models.CharField(max_length=255)
