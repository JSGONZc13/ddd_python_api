from domain.repository.product_repository import ProductRepository
from infrastructure.repository_impl.product_repository_impl import ProductRepositoryImpl


class DelProduct:
    def __init__(self):
        self.product_repository:ProductRepository = ProductRepositoryImpl()

    def execute(self, product_id):
        self.product_repository.delete(product_id)