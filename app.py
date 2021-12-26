from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, request, redirect, make_response      
from settings import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

#...


#...


def init_app():
     db.create_all() 
     return app

app = init_app()

# ROUTES

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/explain")
def about():
    return render_template("explain.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/addentry", methods=["POST"])
def truc():
    print(request.form)
    valeur = request.form
    newdep = Transaction(
        valeur['montant'], 'all good', 'all good')
    db.session.add(newdep)
    db.session.commit()
    return redirect(url_for('budget_bp.seedb'))


@app.route("/dashboard_with_stuff")
def dashboard_with_stuff():
    depenses = Transaction.query.all()
    deps = []
    for depense in depenses:
        print("Amount = " + str(depense.amount))
        dep = {"amount": depense.amount}
        deps.append(dep)
    print(deps)
    return render_template("dashboard_with_stuff.html", depenses=deps)
    
    
@app.route("/essai")
def essai():
    return "Hello"

@app.route("/reset_db")
def reset_db():
    db.drop_all()
    db.create_all()
    return "Database reset"

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "T'es perdu"
    
if __name__ == "__main__":
    app.run(debug=True)


# MODEL