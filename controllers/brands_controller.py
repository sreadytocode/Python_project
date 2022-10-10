from crypt import methods
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.brand import Brand
import repositories.brand_repository as brand_repository
import repositories.garment_repository as garment_repository
import repositories.image_repository as image_repository

brands_blueprint = Blueprint("brands", __name__)

@brands_blueprint.route("/brands")
def brands():
    brands = brand_repository.select_all()
    return render_template("brands/index.html", brands = brands)

@brands_blueprint.route("/brands", methods=['POST'])
def create_brand():
    name = request.form['brand_name']
    brand = Brand(name)
    brand_repository.save(brand)

    return redirect("/brands")

@brands_blueprint.route("/brands/<id>", methods=['GET'])
def individual_brand(id):
    brand = brand_repository.select(id)
    return render_template("brands/individual.html", brand = brand)

@brands_blueprint.route("/brands/<id>/edit", methods=['GET'])
def edit_brand(id):
    brand = brand_repository.select(id)
    return render_template("brands/edit.html", brand = brand)

@brands_blueprint.route("/brands/<id>", methods=['POST'])
def update_brand_details(id):
    name = request.form['name']
    brands = Brand(name, id)
    brand_repository.update(brands)

    return redirect("/brands")

@brands_blueprint.route("/brands/<id>/delete", methods=['POST'])
def delete_brand(id):
    brand_repository.delete(id)
    return redirect("/brands")

@brands_blueprint.route("/brands/<id>/garments", methods=['GET'])
def get_brand_garments(id):
    images = image_repository.select_all()
    garments = garment_repository.select_all()
    brand = brand_repository.select(id)

    return render_template("brands/connecting.html", images = images, garments = garments, brand = brand)