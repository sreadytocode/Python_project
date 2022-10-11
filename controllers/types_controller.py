from crypt import methods
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.garment import Garment
import repositories.garment_repository as garment_repository
import repositories.brand_repository as brand_repository
import repositories.image_repository as image_repository
import repositories.type_repository as type_repository

types_blueprint = Blueprint("types", __name__)