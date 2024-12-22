from flask import Flask, request, jsonify,Blueprint
from pymongo import MongoClient
from dotenv import load_dotenv
from config import DevelopmentConfig, ProductionConfig
from db import db
import os


if os.getenv('FLASK_ENV') == 'production':
    active_config = ProductionConfig
else:
    active_config = DevelopmentConfig


about_collection = db['abouts']

about_bp = Blueprint('about', __name__, url_prefix='/about')

def get_about():
    try:
        about = list(about_collection.find({},{'_id':0}))
        return jsonify(about)
    except Exception as e :
        return jsonify({"error" : str(e)}),500