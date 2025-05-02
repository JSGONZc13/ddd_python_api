# app/api/product_controller.py
from flask import Blueprint, request, jsonify
from domain.entities.product import Product
from application.use_cases.add_product import AddProduct
from application.use_cases.del_product import DelProduct
from application.use_cases.get_product import GetProduct
from application.use_cases.get_products import GetProducts

product_api = Blueprint("product_api", __name__)

# Initialize ProductService with the in-memory repository
_add_product = AddProduct()
_get_product = GetProduct()
_get_products = GetProducts()
_del_product = DelProduct()


@product_api.route("/ADD_PRODUCT", methods=["POST"])
def create():
    data = request.get_json()
    product_ = Product(name=data["name"], price=data["price"])
    response = _add_product.execute(product_)
    return jsonify(response), 200

@product_api.route("/GET_PRODUCT", methods=["POST"])
def get_product():
    data = request.get_json()
    id = data.get("id")
    response = _get_product.execute(id)
    return jsonify(response), 200

@product_api.route("/DEL_PRODUCT", methods=["POST"])
def delete_product():
    data = request.get_json()
    id = data.get("id")
    response = _del_product.execute(id)
    return jsonify(response), 200

@product_api.route("/GET_PRODUCTS", methods=["POST"])
def get_products():
    response  = _get_products.execute()
    return jsonify(response), 200