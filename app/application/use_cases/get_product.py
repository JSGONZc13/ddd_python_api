from domain.repository.product_repository import ProductRepository
from infrastructure.repository_impl.product_repository_impl import ProductRepositoryImpl


class GetProduct:
     def __init__(self):
          self.product_repository:ProductRepository = ProductRepositoryImpl()
     
     def execute(self, product_id):
          return self.product_repository.get_by_id(product_id)