# Tp Django
Architecture du projet listecourse :  

```
listecourse  
|
|---migration
|   |   0001_initial.py : Fichier de migration de la BDD V1
|   |   002_liste.py : Fichier de migration de la BDD V2
|   |   0003_produit_illustration.py : Fichier de migration de la BDD V3
|
|---models
|   |   produit.py : Fichier qui correspond à la table produit
|   |   liste.py : FIchier qui correspond à la table liste
|
|---templates
|   |   listecourse
|   |   |   accueil.html : Html pour la vue accueil
|   |   |   addProduct.html : Html pour la vue addProduct
|   |   |   addProductInList.html : Html pour la vue addProductInList
|   |   |   login.html : Html pour la vue login
|   |   |   registration.html : Html pour la vue registration
|
|---views
|   |   accueil.py : Vue de la page accueil
|   |   addProduct.py : Vue de la page addProduct
|   |   addProductInList.py : Vue de la page addProductInList
|   |   login.py : Vue de la page login
|   |   logout.py : Méthode pour la déconnexion
|   |   registration.py : Vue de la page d'inscription
|
|   admin.py : Fichier de configuration pour l'administration
|   apps.py : Fichier de déclaration de l'application
|   tests.py : Fichier qui contient les tests de l'application
|   urls.py : Fichier contenant l'ensemble des urls de l'application
```

Fichier modifié :
- **accueil.html** 
- **addProduct.html** 
- **liste.py**
- **accueil.py**
- **addProduct.py**
- **urls.py**

Si vous reprenez le projet à partir de cette correction supprimer le fichier db.sqlite3 si existant 
et exécuter cette commande : `python manage.py migrate`

Pour créer le super utilisateur voici la commande : `python manage.py createsuperuser`