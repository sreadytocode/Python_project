from crypt import methods
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.type import Type
import repositories.garment_repository as garment_repository
import repositories.brand_repository as brand_repository
import repositories.image_repository as image_repository
import repositories.type_repository as type_repository

types_blueprint = Blueprint("types", __name__)

@types_blueprint.route("/types")
def types():
    types = type_repository.select_all()
    return render_template("types/index.html", types = types)

@types_blueprint.route("/types", methods=['POST'])
def create_type():
    type_type = request.form['type_type']
    type = Type(type_type)
    type_repository.save(type)

    return redirect("/types")

@types_blueprint.route("/types/<id>", methods=['GET'])
def individual_garment_type(id):
    images = image_repository.select_all()
    garments = garment_repository.select_all()
    brands = brand_repository.select_all()
    type = type_repository.select(id)
    return render_template("types/individual.html", type = type, brands = brands, garments = garments, images = images)

@types_blueprint.route("/types/<id>/edit", methods=['GET'])
def edit_type(id):
    type = type_repository.select(id)
    return render_template("types/edit.html", type = type)

@types_blueprint.route("/types/<id>", methods=['POST'])
def update_type_details(id):
    type_type = request.form['type_type']
    types = Type(type_type, id)
    type_repository.update(types)

    return redirect("/types")

@types_blueprint.route("/types/<id>/delete", methods=['POST'])
def delete_type(id):
    type_repository.delete(id)
    return redirect("/types")