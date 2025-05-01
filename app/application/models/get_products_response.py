from domain.entities.product import Product
from application.models.api_response import ApiResponse


class GetProductsResponse(ApiResponse):
     def __init__(self, code: int, message: str, products: list[Product]):
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
               return GetProductsResponse(
                    code=1,
                    message="No hay productos registrados",
                    products=[]
                    )
          
          
          return GetProductsResponse(
               code=0,
               message="Productos obtenidos correctamente",
               products=products
          )

     @staticmethod
     def error(message: str):
          return GetProductsResponse(
               code=2,
               message=message,
               products=[]
          )