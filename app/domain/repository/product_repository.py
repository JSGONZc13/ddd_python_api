from abc import ABC, abstractmethod
from domain.entities.product import Product


class ProductRepository(ABC):
     @abstractmethod
     def save(self, product: Product) -> Product:
          pass
     
     @abstractmethod
     def get_by_id(self, product_id: int) -> Product | None:
          pass

     @abstractmethod
     def delete(self, product_id: int) -> None:
          pass
     
     @abstractmethod
     def get_all(self) -> list[Product]:
          pass