from flask import Blueprint, render_template, request, redirect, url_for
from .models import Product
from .. import db

advert = Blueprint('advert', __name__, template_folder='templates')


@advert.route('/add', methods=['POST'])
def add():
    prod_name = request.form['product_name']
    prod_price = request.form['product_price']
    prod_quantity = request.form['product_quantity']
    print(prod_name)
    print(prod_price)
    print(prod_quantity)

    new_product = Product(name=prod_name, price=prod_price, quantity=prod_quantity)
    if prod_name == '' or prod_price == '' or prod_quantity == '':
        print('Enter product name, price and quantity')
    else:
        db.session.add(new_product)
        print('Product has been added')
        db.session.commit()
    return render_template("home.html")


@advert.route('/product_list', methods=['GET', 'POST'])
def product_list():
    pass

