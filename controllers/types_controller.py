from crypt import methods
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.garment import Garment
import repositories.garment_repository as garment_repository
import repositories.brand_repository as brand_repository
import repositories.image_repository as image_repository
import repositories.type_repository as type_repository

types_blueprint = Blueprint("types", __name__)

@types_blueprint.route("/types/<id>", methods=['GET'])
def filter_type(id):
    types = type_repository.select_all()
    brands = brand_repository.select_all()
    garments = garment_repository.select(id)
    images = image_repository.select_all()
    return render_template("types/index.html", types = types, brands = brands, garments = garments, images = images)

