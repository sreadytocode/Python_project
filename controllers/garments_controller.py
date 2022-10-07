from crypt import methods
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.garment import Garment
import repositories.garment_repository as garment_repository
import repositories.brand_repository as brand_repository

garments_blueprint = Blueprint("garments", __name__)

@garments_blueprint.route("/garments")
def garments():
    garments = garment_repository.select_all()
    return render_template("garments/index.html", garments = garments)

@garments_blueprint.route("/garments", methods=['POST'])
def create_garment():
    brand_id = request.form['brand_id']
    name = request.form['name']
    description = request.form['description']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    brand = brand_repository.select(brand_id)
    garment = Garment(name, brand, description, stock_quantity, buying_cost, selling_price)
    garment_repository.save(garment)
    
    return redirect("/garments")

