from crypt import methods
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.garment import Garment
import repositories.garment_repository as garment_repository
import repositories.brand_repository as brand_repository
import repositories.image_repository as image_repository

images_blueprint = Blueprint("images", __name__)

@images_blueprint.route("/imgs/<path>")
def images(path):
    garment = garment_repository.select_all()
    brands = brand_repository.select_all()
    images = image_repository.select(path)
    return render_template("garments/individual.html", garment = garment, brands = brands, images = images)
