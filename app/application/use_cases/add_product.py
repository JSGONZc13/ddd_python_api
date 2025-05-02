from application.models.add_product_res import AddProductRes
from domain.repository.product_repository import ProductRepository
from domain.entities.product import Product
from infrastructure.repository_impl.product_repository_impl import ProductRepositoryImpl


class AddProduct:
    def __init__(self):
        self.product_repository:ProductRepository = ProductRepositoryImpl()

    def execute(self, product:Product) -> Product:
        try:
            product = self.product_repository.save(product)
            return AddProductRes.from_product(product).to_dict()
        except Exception as e:
            return AddProductRes.error(f"Error al agregar producto: {str(e)}").to_dict()
