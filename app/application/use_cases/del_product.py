from domain.repository.product_repository import ProductRepository
from infrastructure.repository_impl.product_repository_impl import ProductRepositoryImpl
from application.models.del_product_res import DelProductRes

class DelProduct:
    def __init__(self):
        self.product_repository: ProductRepository = ProductRepositoryImpl()

    def execute(self, product_id: int):
        try:
            model = self.product_repository.get_by_id(product_id)
            if model:
                self.product_repository.delete(product_id)
                return DelProductRes.success().to_dict()
            else:
                return DelProductRes.not_found().to_dict()
        except Exception as e:
            return DelProductRes.error(f"Error al eliminar producto: {str(e)}").to_dict()