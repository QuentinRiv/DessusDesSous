from flask.templating import render_template
from flask import render_template, url_for, request, redirect
from flask import request, Blueprint, jsonify
from flask import current_app as app
from .models import db, Transaction, User, Category
from collections import defaultdict  # available in Python 2.5 and newer
from flask_login import login_required, current_user

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

@budget_bp.route("/add_money", methods=["POST"])
def truc():
    req = request.get_json()
    print(req)
    newdep = Transaction(
        req['amount'], req['category'], req['comment'])
    db.session.add(newdep)
    db.session.commit()
    return {"Answer " : "Alright"}, 200

@budget_bp.route("/getdata")
def getdata():
    trans_d = defaultdict(int)
    transactions = Transaction.query.all()
    for transaction in transactions:
        trans_d[transaction.category] += transaction.amount

    print("\n----Dico :", trans_d)

    return jsonify(trans_d)
    
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