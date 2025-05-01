class ApiResponse:
     def __init__(self, code: int, message: str):
          self.code = code
          self.message = message
     
     def to_dict(self):
          return {
               "code": self.code,
               "message": self.message
               }
     @classmethod
     def error(cls, message: str):
          return cls(code=2, message=message)