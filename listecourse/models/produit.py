from django.db import models


class Produit(models.Model):
    nomProduit = models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return self.nomProduit
