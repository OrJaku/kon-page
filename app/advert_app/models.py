from app import db


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    price = db.Column(db.Float(10), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500))


    def __repr__(self):

        return f'{self.name} {self.price} {self.id}'