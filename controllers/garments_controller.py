from crypt import methods
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.garment import Garment
import repositories.garment_repository as garment_repository
import repositories.brand_repository as brand_repository
import repositories.image_repository as image_repository

garments_blueprint = Blueprint("garments", __name__)

@garments_blueprint.route("/garments", methods=['GET'])
def new_garment():
    brands = brand_repository.select_all()
    garments = garment_repository.select_all()
    images = image_repository.select_all()
    return render_template("garments/index.html", garments = garments, brands = brands, images = images)

@garments_blueprint.route("/garments", methods=['POST'])
def create_garment():
    name = request.form['name']
    brand_id = request.form['brand']
    description = request.form['description']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    brands = brand_repository.select(brand_id)
    garment = Garment(name, brands, description, stock_quantity, buying_cost, selling_price)
    garment_repository.save(garment)
    
    return redirect("/garments")

@garments_blueprint.route("/garments/<id>", methods=['GET'])
def individual_garment(id):
    garment = garment_repository.select(id)
    brands = brand_repository.select_all()
    images = image_repository.select_all()
    return render_template("garments/individual.html", garment = garment, brands = brands, images = images)

@garments_blueprint.route("/garments/<id>/edit", methods=['GET'])
def edit_garment(id):
    garment = garment_repository.select(id)
    brands = brand_repository.select_all()
    images = image_repository.select_all()
    return render_template("garments/edit.html", garment = garment, brands = brands, images = images)

@garments_blueprint.route("/garments/<id>", methods=['POST'])
def update_details(id):
    name = request.form['name']
    brands = request.form['brands']
    description = request.form['description']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    brands = brand_repository.select(brands)
    markup = garment_repository.select(markup)
    garment = Garment(name, brands, description, stock_quantity, buying_cost, selling_price, markup, id)
    garment_repository.update(garment)

    return redirect("/garments")

@garments_blueprint.route("/garments/<id>/delete", methods=['POST'])
def delete_garment(id):
    garment_repository.delete(id)
    return redirect("/garments")


    



