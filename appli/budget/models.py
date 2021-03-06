from flask_login import UserMixin
from appli import db
from time import time

# Contient les Tables
# Puis les classes si on en fait


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    money = db.Column(db.Integer)
    piggy_bank = db.Column(db.Integer)
    debt = db.Column(db.Integer)

    def __init__(self, email, password, username=None, money=0,
                 piggy_bank=None, debt=None):
        self.username = username
        self.password = password
        self.email = email
        self.money = money
        self.piggy_bank = piggy_bank
        self.debt = debt

    def __repr__(self):
        return '<User %r>' % self.username

    def content(self):
        return {k: self.__dict__[k] for k in sorted(self.__dict__) if '_sa_' != k[:4]}


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    assigned = db.Column(db.Integer)
    spent = db.Column(db.Integer)
    available = db.Column(db.Integer)



    def __init__(self, name, username=None, assigned=300,
                 spent=0, available=300):
        self.name = name
        self.username = username
        self.assigned = assigned
        self.spent = spent
        self.available = available


    def __repr__(self):
        return '<Category %r>' % self.name

    def content(self):
        return {k: self.__dict__[k] for k in sorted(self.__dict__) if '_sa_' != k[:4]}



class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50))
    comment = db.Column(db.String(50))
    origin_category_id = db.Column(db.String(50))
    destination_category_id = db.Column(db.String(50))
    date = db.Column(db.String(50))

    def __init__(self, amount, category, comment, origin_category_id=None, destination_category_id=None, date=None):
        self.amount = amount
        self.date = date
        self.comment = comment
        self.category = category
        self.origin_category_id = origin_category_id
        self.destination_category_id = destination_category_id

    def __repr__(self):
        return '<Transaction %r>' % self.category

    def content(self):
        return {k: self.__dict__[k] for k in sorted(self.__dict__) if '_sa_' != k[:4]}
