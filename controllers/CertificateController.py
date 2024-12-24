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
    
def get_certificate_detail(slug):
    try:
        certificate_detail = certificate_collection.find_one({ "slug": slug},{'_id':0})
        return jsonify({"data":certificate_detail})
    except Exception as e:
        return jsonify({"error": str(e)}),500