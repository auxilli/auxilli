# auxillia api documentation

## Getting Started

### Installation des Dépendances

#### Python 3.10.0
#### pip 21.3.1 from C:\Users\hp\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)

Suivez les instructions suivantes pour installer l'ancienne version de python sur la plateforme [python docs](https://www.python.org/downloads/windows/#getting-and-installing-the-latest-version-of-python)

#### Dépendances de PIP

Pour installer les dépendances, ouvrez le dossier `/Documentation` et exécuter la commande suivante:

```bash ou powershell ou cmd
pip install -r requirements.txt
or
pip3 install -r requirements.txt
```

Nous passons donc à l'installation de tous les packages se trouvant dans le fichier `requirements.txt`.

##### clé de Dépendances

- [Flask](http://flask.pocoo.org/)  est un petit framework web Python léger, qui fournit des outils et des fonctionnalités utiles qui facilitent la création d’applications web en Python.

- [SQLAlchemy](https://www.sqlalchemy.org/) est un toolkit open source SQL et un mapping objet-relationnel écrit en Python et publié sous licence MIT. SQLAlchemy a opté pour l'utilisation du pattern Data Mapper plutôt que l'active record utilisés par de nombreux autres ORM

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Démarrer le serveur

Pour démarrer le serveur sur Linux ou Mac, executez:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
Pour le démarrer sur Windows, executez:

```bash
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
``` 

## API REFERENCE

Getting starter

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://localhost:5000; which is set as a proxy in frontend configuration.

## Type d'erreur
Les erreurs sont renvoyées sou forme d'objet au format Json:
{
    "success":False
    "error": 400
    "message":"Ressource non disponible"
}

L'API vous renvoie 4 types d'erreur:
. 400: Bad request ou ressource non disponible
. 500: Internal server error
. 422: Unprocessable
. 404: Not found

## Endpoints
. ## GET/livres

    GENERAL:
        Cet endpoint retourne la liste des objets livres, la valeur du succès et le total des livres. 
    
        
    EXEMPLE: curl http://localhost:5000/livres
```
       {
    
    "Livre": [
        {
            "Auteur": "Auteur1",
            "Categorie_livre": "Action",
            "Date_publication": "10-10-2010",
            "Editeur": "editeur1",
            "Id": 1,
            "Isbn": "JHY",
            "Titre": "Titre1"
        },
        {
            "Auteur": "AuTORr1",
            "Categorie_livre": "danger",
            "Date_publication": "10-10-2010",
            "Editeur": "edit",
            "Id": 2,
            "Isbn": "ayyY",
            "Titre": "Titré2"
        },
        {
            "Auteur": "Auteur1",
            "Categorie_livre": "sexuel",
            "Date_publication": "10-10-2000",
            "Editeur": "e1",
            "Id": 3,
            "Isbn": "youY",
            "Titre": "losangeles1"
        }
    ],
    "nombre Total de Livres": 3,
    "success": true
}

```

.##GET/livres(id)
  GENERAL:
  Cet endpoint permet de récupérer les informations d'un livre particulier s'il existe par le biais de l'ID.

    EXEMPLE: http://localhost:5000/livres/1
```
    {
        "Livre": {
        "Auteur": "Auteur1",
        "Categorie_livre": "Action",
        "Date_publication": "10-10-2010",
        "Editeur": "editeur1",
        "Id": 1,
        "Isbn": "JHY",
        "Titre": "Titre1"
    },
    "success": true
    }
```


. ## DELETE/livres (id)

    GENERAL:
        Supprimer un element si l'ID existe. Retourne l'ID du livre supprimé, la valeur du succès et le nouveau total.

        EXEMPLE: curl -X DELETE http://localhost:5000/books/5
```
{
   
    "Livre_restant": 2,
    "deleted_id": 1,
    "success": true
}
```

. ##PATCH/livres(id)
  GENERAL:
  Cet endpoint permet de mettre à jour, le titre, l'auteur, et l'éditeur du livre.
  Il retourne un livre mis à jour.

  EXEMPLE.....Avec Patch
  ``` curl -X PATCH http://localhost:5000/livres/3 -H "Content-Type:application/json" -d '{"auteur": "Azychika, Takumi Fukui","editeur": "Ki-oon","titre": "Jujutsu Kaisen"}'
  ```
  ```
    {
        
    "Livre_modifie": {
        "Auteur": "auxillia",
        "Categorie_livre": "Action",
        "Date_publication": "10-10-2010",
        "Editeur": "editeur1",
        "Id": 1,
        "Isbn": "JHY",
        "Titre": "Titre1"
    },
    "success": true
    }
    ```

. ## GET/categories

    GENERAL:
        Cet endpoint retourne la liste des categories de livres, la valeur du succès et le total des categories disponibles. 
    
        
    EXEMPLE: curl http://localhost:5000/categories

        {
     "Categorie": [
        {
            "id": 1,
            "libelle_categorie": "Action"
        },
        {
            "id": 2,
            "libelle_categorie": "danger"
        },
        {
            "id": 3,
            "libelle_categorie": "sexuel"
        }
    ],
    "nombre Total de categorie": 3,
    "success": true
}
```

.##GET/categories(categorie_id)
  GENERAL:
  Cet endpoint permet de récupérer les informations d'une categorie si elle existe par le biais de l'ID.

    EXEMPLE: http://localhost:5000/categories/1
```
  {
    
    "Categorie": {
        "id": 1,
        "libelle_categorie": "Action"
    },
    "success": true
}
```

. ## DELETE/categories (categorie_id)

    GENERAL:
        Supprimer un element si l'ID existe. Retourne l'ID da la catégorie supprimé, la valeur du succès et le nouveau total.

        EXEMPLE: curl -X DELETE http://localhost:5000/categories/4
```
{
     "Categories_restantes": 3,
    "id_cat_deleted": 4,
    "status": 200,
    "success": true
}
```



. ##############PATCH/categories(categorie_id)#################

  GENERAL:
  Cet endpoint permet de mettre à jour le libelle ou le nom de la categorie.
  Il retourne une nouvelle categorie avec la nouvelle valeur.

  EXEMPLE.....Avec Patch
  ``` curl -X PATCH 'http://localhost:5000/categories/1' -H "Content-Type:application/json" -d '{"categorie": "Histoire"}'
  ```
  ```
    {
         
    "Categorie_Modifie": {
        "id": 1,
        "libelle_categorie": "Action"
    },
    "success": true
    }

.##GET/livres/categories(categorie_id)
  GENERAL:
  Cet endpoint permet de lister les livres appartenant à une categorie donnée.
  Il renvoie la classe de la categorie et les livres l'appartenant.

    EXEMPLE: http://localhost:5000/livres/categories/4.
```
    {

    "Livre": [
        {
            "Auteur": "auxillia",
            "Categorie_livre": "Action",
            "Date_publication": "10-10-2010",
            "Editeur": "editeur1",
            "Id": 1,
            "Isbn": "JHY",
            "Titre": "Titre1"
        }
    ],
    "Nombre de livre de la categorie ": 1,
    "success": true
}
```

