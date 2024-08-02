from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.db"
# Secret key for session management and CSRF protection
app.config['SECRET_KEY'] = 'your_secret_key_here'

db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()

# Route for creating a new product
@app.route("/product", methods=["POST"])
def create_product():
    data = request.get_json()
    name = data.get("name")
    price = data.get("price")
    if not name or not price:
        return jsonify({"error": "Name and price are required"}), 400
    try:
        price = float(price)
    except ValueError:
        return jsonify({"error": "Price must be a number"}), 400
    new_product = Product(name=name, price=price)
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product created successfully", "product": {"id": new_product.id, "name": new_product.name, "price": new_product.price}}), 201

# Route for retrieving all products
@app.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    products_list = [{"id": product.id, "name": product.name, "price": product.price} for product in products]
    return jsonify(products_list), 200

# Route for retrieving a single product by ID
@app.route("/product/<int:id>", methods=["GET"])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify({"id": product.id, "name": product.name, "price": product.price}), 200

# Route for updating a product by ID
@app.route("/product/<int:id>", methods=["PUT"])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    name = data.get("name")
    price = data.get("price")
    if not name or not price:
        return jsonify({"error": "Name and price are required"}), 400
    try:
        price = float(price)
    except ValueError:
        return jsonify({"error": "Price must be a number"}), 400
    product.name = name
    product.price = price
    db.session.commit()
    return jsonify({"message": "Product updated successfully", "product": {"id": product.id, "name": product.name, "price": product.price}}), 200

# Route for deleting a product by ID
@app.route("/product/<int:id>", methods=["DELETE"])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted successfully"}), 200

if __name__ == "__main__":
    
    app.run(debug=True, host='0.0.0.0')
