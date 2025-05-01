from domain.repository.product_repository import ProductRepository
from infrastructure.data_source.product_data_source import ProductDataSource
from domain.entities.product import Product
from infrastructure.models.product_model import ProductModel

class ProductRepositoryImpl(ProductRepository):
     def __init__(self):
        self.datasource = ProductDataSource()

     def save(self, product: Product) -> Product:
          if product.id:
               model = self.datasource.get(int(product.id))
               if model:
                    model.strName = product.name
                    model.fltPrice = product.price
               else:
                    model = ProductModel.from_domain(product)
          else:
               model = ProductModel.from_domain(product)
          self.datasource.save(model)
          return model.to_domain()
     
     def get_by_id(self, product_id: int) -> Product | None:
          model = self.datasource.get(product_id)
          return model.to_domain() if model else None

     def delete(self, product_id: int):
          model = self.datasource.get(product_id)
          if model:
               self.datasource.delete(model)
     
     def get_all(self) -> list[Product]:
          models = self.datasource.getAll()
          return [model.to_domain() for model in models] if models else []