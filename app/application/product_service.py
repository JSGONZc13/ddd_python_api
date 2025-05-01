# app/application/product_service.py
from domain.entities.product import Product
from infrastructure.repository.product_repository import ProductRepository

class ProductService:
     def __init__(self, repository: ProductRepository):
          self.repository = repository

     def create_product(self, name: str, price: float) -> Product:
          product = Product(id=None, name=name, price=price)
          return self.repository.save(product)

     def get_product(self, product_id: int) -> Product:
          return self.repository.get_by_id(product_id)

     def update_product(self, product_id: int, name: str, price: float) -> Product:
          product = self.repository.get_by_id(product_id)
          product.name = name
          product.price = price
          return self.repository.save(product)

     def delete_product(self, product_id: int):
          self.repository.delete(product_id)
