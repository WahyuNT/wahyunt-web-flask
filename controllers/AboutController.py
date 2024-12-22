from flask import Flask, request, jsonify,Blueprint
from pymongo import MongoClient
from dotenv import load_dotenv
from config import DevelopmentConfig, ProductionConfig
from db import db
import os



about_collection = db['abouts']

def get_about():
    try:

        about = list(about_collection.find({}, {'_id': 0}))
        return jsonify({"data": about}), 200
    except Exception as e :
        return jsonify({"error" : str(e)}),500
    
    