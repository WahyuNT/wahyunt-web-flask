from flask import Flask, request, jsonify,Blueprint
from pymongo import MongoClient
from dotenv import load_dotenv
from config import DevelopmentConfig, ProductionConfig
from db import db
import os



about_collection = db['abouts']

def get_about():
    try:
        about = about_collection.find_one({},{'_id':0})
        return jsonify(about)
    except Exception as e :
        return jsonify({"error" : str(e)}),500