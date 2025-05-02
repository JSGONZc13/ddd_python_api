from domain.entities.product import Product
from application.models.api_response import ApiResponse

class AddProductRes(ApiResponse):
     def __init__ (self, code: int, message: str, product: Product = None):
          super().__init__(code, message)
          self.product = self._to_dict(product) if product else None
     
     def _to_dict(self, product: Product):
          return {
               "id": product.id,
               "name": product.name,
               "price": product.price
          }
     
     def to_dict(self):
          base = super().to_dict()
          base["product"] = self.product
          return base
     
     @staticmethod
     def from_product(product: Product):
          if not product:
               return AddProductRes(
                    code=1,
                    message="No se pudo registrar el producto",
                    product=None
               )
          
          return AddProductRes(
               code=0,
               message="Producto registrado correctamente",
               product=product
          )