from flask import Blueprint, render_template, request
from .. import db
from ..advert_app.models import Product

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def home():
    products_id = db.session.query(Product.id).all()
    products_id = ([x[0] for x in products_id])
    products_id = sorted(products_id)
    products_list = []
    for i in products_id:
        product = Product.query.filter_by(id=i).first()
        products_list.append(product)
    return render_template("home.html", products_list=products_list)

