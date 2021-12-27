from flask_login import UserMixin
from appli import db
from time import time

# Contient les Tables
# Puis les classes si on en fait


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
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


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    amount_assigned = db.Column(db.Integer)
    amount_spent = db.Column(db.Integer)
    amount_available = db.Column(db.Integer)



    def __init__(self, id, category_name, username=None, amount_assigned=None,
                 amount_spent=None, amount_available=None):
        self.id = id
        self.category_name = category_name
        self.username = username
        self.amount_assigned = amount_assigned
        self.amount_spent = amount_spent
        self.amount_available = amount_available


    def __repr__(self):
        return '<Category %r>' % self.category_name


class Transaction(db.Model):
    __tablename__ = 'transaction'
    transaction_id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    transaction_type = db.Column(db.String(50))
    comment = db.Column(db.String(50))
    origin_category_id = db.Column(db.String(50))
    destination_category_id = db.Column(db.String(50))

    # category = user_id = db.Column(db.Integer, db.ForeignKey('list.category_id'),
    #                                nullable=False)
    date = db.Column(db.String(50))
    category = db.Column(db.String(50), nullable=False)

    def __init__(self, transaction_id, amount, transaction_type, comment, origin_category_id, destination_category_id, date):
        self.id = transaction_id
        self.amount = amount
        self.date = date
        self.comment = comment
        self.transaction_type = transaction_type
        self.origin_category_id = origin_category_id
        self.destination_category_id = destination_category_id

    def __repr__(self):
        return '<Transaction %r>' % self.category_name
