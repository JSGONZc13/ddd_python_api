from infrastructure.models.product_model import ProductModel
from infrastructure.database.database import db
class ProductDataSource:
     def __init__(self):
          self.model = ProductModel
     
     def get(self, id_:int)-> ProductModel | None:
          return db.session.get(self.model, id_)
     
     def getAll(self) -> list[ProductModel]:
          return db.session.query(self.model).all()

     def save(self, instance: ProductModel)-> ProductModel:
          db.session.add(instance)
          db.session.commit()
          return instance

     def delete(self, instance: ProductModel) -> None:
          db.session.delete(instance)
          db.session.commit()