from flask import Flask,jsonify,abort,request
from flask_migrate import Migrate
from flask_sqlalchemy import Pagination, SQLAlchemy 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:    @localhost:5432/projet"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS,PATCH')
    return response


class Categorie(db.Model):
    __tablename__ = 'Categories'
    id = db.Column(db.Integer, primary_key=True)
    libelle_categorie = db.Column(db.String(50), nullable=False)
    def __init__(self, libelle_categorie):
        self.libelle_categorie = libelle_categorie

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        #db.session.commit()
    def format(self):
        return {
            'id': self.id,
            'libelle_categorie': self.libelle_categorie
        }


class Livre(db.Model):
    __tablename__ = 'Livres'
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(50), nullable=False)
    titre = db.Column(db.String(100), unique=True)
    date_publication = db.Column(db.String(12), nullable=False)
    auteur = db.Column(db.String(50),nullable=False)
    editeur = db.Column(db.String(50),nullable=False)
    categorie_id = db.Column(db.Integer,  db.ForeignKey(Categorie.id) )
    def __init__(self, isbn, titre,date_publication,auteur,editeur,categorie_id):
        self.isbn=isbn
        self.titre=titre
        self.date_publication=date_publication
        self.auteur=auteur
        self.editeur=editeur
        self.categorie_id=categorie_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        #db.session.commit()

    def format(self):
        c1=Categorie.query.get(self.categorie_id)
        return {
            'Id': self.id,
            'Isbn': self.isbn,
            'Titre': self.titre,
            'Date_publication': self.date_publication,
            'Auteur': self.auteur,
            'Editeur': self.editeur,
            'Categorie_livre': c1.libelle_categorie
        }
        
db.create_all()



#######################################
    # Lister toutes les categories
#######################################


@app.route("/categories")
def get_all_cats():
    cat = Categorie.query.all()
    cat = [c.format() for c in cat]
    return jsonify(

        {
            
            'success': True,
            'Categorie': cat,
            'nombre Total de categorie': len(Categorie.query.all())

        }

    )



##############################
# Lister tous les livres
##############################


@app.route("/livres/")
def get_all_liv():
    l = Livre.query.all()
    l = [c.format() for c in l]
    return jsonify(

        {

            'success': True,
            'Livre': l,
            'nombre Total de Livres': len(Livre.query.all())

        }

    )



#################################################
## Chercher un livre en particulier par son id
#################################################


@app.route('/livres/<int:ID>')
def get_one_liv(ID):
    try:
        l1 = Livre.query.get(ID)
        return jsonify(
            {
                'success': True,
                'Livre': l1.format()
            }
        )  
    except:
        abort(400)


 ########################################
# Chercher une categorie par son id
########################################

@app.route('/categories/<int:ID>')
def get_one_cat(ID):
    try:
        c1 = Categorie.query.get(ID)
        return jsonify(
            {
                'success': True,
                'Categorie': c1.format()
            }
        )  
    except:
        abort(400)


################################################
## Lister les livres d'une categorie
################################################


@app.route('/categories/<int:ID>/livres')
def get_liv_cat(ID):
    x=Livre.query.filter(Livre.categorie_id==ID).all()        
    try:
        return jsonify(
            {
                'success': True,
                'Livre': [c.format() for c in x],
                'Nombre de livre de la categorie ':len(x)
            }
        )  
    except:
        abort(400)  

###########################################
    # Modifier les informations d'un livre
###########################################

@app.route('/livres/<int:id>', methods=['PATCH'])
def update_liv(id):
    Body = request.get_json()
    book=Livre.query.get(id)
    try:
        if  'Titre'  in Body and 'Isbn' in Body and 'Date_publication' in Body and 'Auteur' in Body and 'Editeur'  in Body:
            book.isbn = Body['Isbn']
            book.titre = Body['Titre']
            book.date_publication = Body['Date_publication']
            book.auteur = Body['Auteur']
            book.editeur = Body['Editeur']
              
        book.update()
        return jsonify({
            'success': True,
            'Livre_modifie': book.format()
        })
    except:
        abort(400)



###########################################
# Modifier les informations d'une categorie
###########################################

@app.route('/categories/<int:id>', methods=['PATCH'])
def update_cat(id):
    Body = request.get_json()
    cat=Categorie.query.get(id)
    try:
        if 'libelle_categorie' in Body :
            cat.libelle_categorie = Body['libelle_categorie']
              
        cat.update()
        return jsonify({
            'success': True,
            'Categorie_Modifie': cat.format()
        })
    except:
        abort(400)

############################
# Supprimer un livre
############################

@app.route('/livres/<int:id>', methods=['DELETE'])
def supprimer_livre(id):
    try:
        mon_livre = Livre.query.get(id)
        if mon_livre is None:
            abort(404)
        else:
            mon_livre.delete()
            return jsonify(
                {
                "success": True,
                "deleted_id": id,
                "Livre_restant": len(Livre.query.all())
                }
            )
    except:
        abort(400)
    finally:
        db.session.close()



#############################
    # Supprimer une categorie
################################# 
           

@app.route('/categories/<int:id>', methods=['DELETE'])
def del_category(id):
        try:
            category = Categorie.query.get(id)
            category.delete()
            return jsonify(
                {       
                'success': True,
                'status': 200,
                'id_cat_deleted': id,
                'Categories_restantes': Categorie.query.count()
                }
            )
        except:
            abort(404)
        finally:
            db.session.close()




@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False, 
        "error": 404,
        "message": "Not found"
        }), 404
    
@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "success": False, 
        "error": 500,
        "message": "Internal server error"
        }), 500


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False, 
        "error": 400,
        "message": "Bad Request"
        }), 400


