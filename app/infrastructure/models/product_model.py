from infrastructure.database.database import db
from domain.entities.product import Product

class ProductModel(db.Model):
    __tablename__ = "products"
    
    intId = db.Column(db.Integer, primary_key=True)
    strName = db.Column(db.String(255), nullable=False)
    fltPrice = db.Column(db.Float, nullable=False)

    def to_domain(self):
         return Product(id=self.intId, name=self.strName, price=self.fltPrice)

    @staticmethod
    def from_domain(product):
         return ProductModel(intId=product.id, strName=product.name, fltPrice=product.price)
