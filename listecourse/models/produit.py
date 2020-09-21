from django.db import models
from django.utils.safestring import mark_safe


class Produit(models.Model):
    nomProduit = models.CharField(primary_key=True, max_length=50)
    illustration = models.ImageField(upload_to='addProduct/', default='addProduct/notfound.jpg')

    def __str__(self):
        return self.nomProduit

