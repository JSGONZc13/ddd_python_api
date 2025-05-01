from domain.repository.product_repository import ProductRepository
from domain.entities.product import Product
from infrastructure.repository_impl.product_repository_impl import ProductRepositoryImpl


class AddProduct:
    def __init__(self):
        self.product_repository:ProductRepository = ProductRepositoryImpl()

    def execute(self, product:Product) -> Product:
        return self.product_repository.save(product)
