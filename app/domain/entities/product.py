class Product:
     def __init__(self, name: str, price: float, id: int = None):
          self.id = id
          self.name = name
          self.price = price

     def __repr__(self):
          return f"<Product id={self.id} name={self.name} price={self.price}>"