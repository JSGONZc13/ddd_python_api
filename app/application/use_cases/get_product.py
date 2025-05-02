from application.models.get_product_res import GetProductRes
from domain.repository.product_repository import ProductRepository
from infrastructure.repository_impl.product_repository_impl import ProductRepositoryImpl


class GetProduct:
     def __init__(self):
          self.product_repository:ProductRepository = ProductRepositoryImpl()
     
     def execute(self, product_id):
          try:
               product = self.product_repository.get_by_id(product_id)
               return GetProductRes.from_product(product).to_dict()
          except Exception as e:
               return GetProductRes.error(f"Error al obtener producto: {str(e)}").to_dict()