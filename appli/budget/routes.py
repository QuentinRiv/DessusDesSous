from flask.templating import render_template
from flask import render_template, url_for, request, redirect
from flask import request, Blueprint, jsonify
from flask import current_app as app
from .models import db, Transaction, User, Category
from collections import defaultdict  # available in Python 2.5 and newer
from flask_login import login_required, current_user
from appli.login.routes import add_db

# Partie lié au budget
# Modifies-y comme tu le sens
# Vu que c'est surtout toi,
# moi je vais pas trop y touché

# Pour l'instant, il y a une page pour
# ajouter une entrée, et une pour les
# afficher


budget_bp = Blueprint('budget_bp', __name__,
                     template_folder='templates',
                     static_folder='static',
                     static_url_path='/appli/budget/static')


@budget_bp.route("/explain")
def about():
    return render_template("explain.html")

@login_required
@budget_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


def update_cat(recipient, amount, origin=None):
    if origin:
        origin_cat = Category.query.filter_by(name=origin).first()
        if origin_cat[0]:
            if origin_cat.assigned > amount:
                origin_cat.assigned -= amount
            else:
                print("Not enough money !")
                return
        else:
            print("Category not found !")
            return
    
    recip_cat = Category.query.filter_by(name=recipient).first()
    if recip_cat[0]:
        recip_cat.assigned += amount
    else:
        print("Category not found !")
        return


@budget_bp.route("/add_money", methods=["POST"])
def add_money():
    req = request.get_json()
    print(req)
    newdep = Transaction(
        req['amount'], req['category'], req['comment'])
    add_db(newdep, "Transaction in {}".format(newdep.category))
    return {"Answer " : "Alright"}, 200


@budget_bp.route("/spend_money", methods=["POST"])
def spend_money():
    req = request.get_json()
    print(req)
    newdep = Transaction(
        req['amount'], req['category'], req['comment'])
    db.session.add(newdep)
    db.session.commit()
    return {"Answer ": "Alright"}, 200

@budget_bp.route("/getdata")
def getdata():
    cat_d = {}
    categories = Category.query.all()
    for category in categories:
        cat_d[category.name] = {"name": category.name, "assigned": category.assigned, "spent": category.spent, "available": category.available}

    print("\n----Dico :", cat_d)

    return jsonify(cat_d)
    

@budget_bp.route("/create_cat", methods=["POST"])
def create_cat():
    req = request.get_json()
    print(req)
    new_cat = Category(name=req['category'],
                       username='Quentin',
                       assigned=int(req['assigned']),
                       spent=int(req['spent']),
                       available=int(req['assigned']) - int(req['spent']))
    add_db(new_cat, "Category in {}".format(new_cat.name))
    return {'Answer': "Okay"}, 200



@budget_bp.route("/essai")
def essai():

    all_users = [user.content() for user in User.query.all()]
    all_categories = [category.content() for category in Category.query.all()]
    all_transactions = [transaction.content() for transaction in Transaction.query.all()]

    all = [all_users, all_categories, all_transactions]
    return render_template("content.html", all=all)

@budget_bp.route("/reset_db")
def reset_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
    return "Database reset"


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("lost.html")