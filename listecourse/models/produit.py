from django.db import models

class Produit(models.Model):
    nomProduit = models.CharField(primary_key=True, max_length=50)