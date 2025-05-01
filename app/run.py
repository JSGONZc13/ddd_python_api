# app/run.py
from flask import Flask
from api.controllers.product_controller import product_api
from infrastructure.database.database import db
def create_app():
     app = Flask(__name__)
     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

     db.init_app(app)
     app.register_blueprint(product_api, url_prefix='/api/product_api')

     with app.app_context():
          from infrastructure.models.product_model import ProductModel
          db.create_all()

     return app

app = create_app()

if __name__ == '__main__':
     app.run(debug=True)
