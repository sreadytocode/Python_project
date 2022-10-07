from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.garment import Garment
import repositories.garment_repository as garment_repository

garments_blueprint = Blueprint("garments", __name__)

@garments_blueprint.route("/garments")
def garments():
    garments = garment_repository.select_all()
    return render_template("garments/index.html", garments = garments)