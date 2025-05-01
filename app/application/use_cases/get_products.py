from application.models.get_products_res import GetProductsRes
from domain.repository.product_repository import ProductRepository
from infrastructure.repository_impl.product_repository_impl import ProductRepositoryImpl


class GetProducts:
     def __init__(self):
          self.product_repository:ProductRepository = ProductRepositoryImpl()
     
     def execute(self):
          try:
               products = self.product_repository.get_all()
               return GetProductsRes.from_products(products).to_dict()
          except Exception as e:
               return GetProductsRes.error(f"Error al obtener productos: {str(e)}").to_dict()