from application.models.api_response import ApiResponse

class DelProductRes(ApiResponse):
     def __init__(self, code: int, message: str):
          super().__init__(code, message)

     @staticmethod
     def success():
         return DelProductRes(
              code=0,
              message="Producto eliminado correctamente"
          )

     @staticmethod
     def not_found():
          return DelProductRes(
               code=1,
               message="Producto no encontrado"
          )