# Tp Django
Architecture du projet listecourse :  

```
listecourse  
|
|---migration
|   |   0001_initial.py : Fichier de migration de la BDD V1
|   |   002_liste.py : Fichier de migration de la BDD V2
|
|---models
|   |   produit.py : Fichier qui correspond à la table produit
|   |   liste.py : FIchier qui correspond à la table liste
|
|---templates
|   |   listecourse
|   |   |   accueil.html : Html pour la vue accueil
|
|---views
|   |   accueil.py : Vue de la page accueil
|
|   admin.py : Fichier de configuration pour l'administration
|   apps.py : Fichier de déclaration de l'application
|   tests.py : Fichier qui contient les tests de l'application
|   urls.py : Fichier contenant l'ensemble des urls de l'application
```

Si vous reprenez le projet à partir de cette correction supprimer le fichier db.sqlite3 si existant 
et exécuter cette commande : `python manage.py migrate`

Pour créer le super utilisateur voici la commande : `python manage.py createsuperuser`