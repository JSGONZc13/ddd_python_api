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
    product = _add_product.execute(product_)
    return jsonify({
        "id": product.id,
        "name": product.name,
        "price": product.price
    }), 201

@product_api.route("/GET_PRODUCT", methods=["POST"])
def get_product():
    data = request.get_json()
    id = data.get("id")
    product = _get_product.execute(id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return (
        jsonify({"id": product.id, "name": product.name, "price": product.price}),
        200,
    )

@product_api.route("/DEL_PRODUCT", methods=["POST"])
def delete_product():
    data = request.get_json()
    id = data.get("id")
    _del_product.execute(id)
    return jsonify({"message": "Product deleted"}), 200

@product_api.route("/GET_PRODUCTS", methods=["POST"])
def get_products():
    products = _get_products.execute()
    return jsonify([{
        "intId": p.id,
        "strName": p.name,
        "fltPrice": p.price
    } for p in products]), 200