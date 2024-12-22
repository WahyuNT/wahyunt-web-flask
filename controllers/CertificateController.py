from flask import Flask, request, jsonify,Blueprint
from pymongo import MongoClient
from dotenv import load_dotenv
from config import DevelopmentConfig, ProductionConfig
from db import db
import os



certificate_collection = db['certificates']

def get_certificate():
    try:
        certificate = list(certificate_collection.find({},{'_id':0}))
        return jsonify({"data":certificate})
    except Exception as e :
        return jsonify({"error" : str(e)}),500
    
    