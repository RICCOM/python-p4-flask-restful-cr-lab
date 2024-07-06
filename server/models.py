from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=True)
    price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)

    def __init__(self, name, image=None, price=0.00):
        self.name = name
        self.image = image
        self.price = price

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'price': str(self.price)  # Converting decimal to string for serialization
        }
