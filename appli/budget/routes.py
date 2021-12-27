from flask.templating import render_template
from flask import render_template, url_for, request, redirect
from flask import request, Blueprint
from flask import current_app as app
from .models import db, Transaction


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

@budget_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@budget_bp.route("/addentry", methods=["POST"])
def truc():
    print(request.form)
    valeur = request.form
    newdep = Transaction(
        valeur['montant'], 'all good', 'all good')
    db.session.add(newdep)
    db.session.commit()
    return redirect(url_for('budget_bp.seedb'))


@budget_bp.route("/dashboard_with_stuff")
def dashboard_with_stuff():
    depenses = Transaction.query.all()
    deps = []
    for depense in depenses:
        print("Amount = " + str(depense.amount))
        dep = {"amount": depense.amount}
        deps.append(dep)
    print(deps)
    return render_template("dashboard_with_stuff.html", depenses=deps)
    
    
@budget_bp.route("/essai")
def essai():
    return "Hello"

@budget_bp.route("/reset_db")
def reset_db():
    db.drop_all()
    db.create_all()
    return "Database reset"

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("lost.html")