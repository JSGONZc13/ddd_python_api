from domain.entities.product import Product
from application.models.api_response import ApiResponse


class GetProductsRes(ApiResponse):
     def __init__(self, code: int, message: str, products: list[Product]=None):
          super().__init__(code, message)
          self.products = [self._to_dict(p) for p in products]
          
     def _to_dict(self, product: Product):
        return {
            "intId": product.id,
            "strName": product.name,
            "fltPrice": product.price
        }
        
     def to_dict(self):
          base = super().to_dict()
          base["products"] = self.products
          return base
     
     @staticmethod
     def from_products(products: list[Product]):
          if not products:
               return GetProductsRes(
                    code=1,
                    message="No hay productos registrados",
                    products=[]
                    )
          
          
          return GetProductsRes(
               code=0,
               message="Productos obtenidos correctamente",
               products=products
          )