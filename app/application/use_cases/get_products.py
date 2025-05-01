from domain.entities.product import Product
from domain.repository.product_repository import ProductRepository
from infrastructure.repository_impl.product_repository_impl import ProductRepositoryImpl


class GetProducts:
    def __init__(self):
        self.product_repository:ProductRepository = ProductRepositoryImpl()

    def execute(self) -> list[Product]:
        return self.product_repository.get_all()