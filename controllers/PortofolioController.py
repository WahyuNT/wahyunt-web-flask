from flask import Flask, request, jsonify,Blueprint
from pymongo import MongoClient
from dotenv import load_dotenv
from config import DevelopmentConfig, ProductionConfig
from db import db
import os



portofolio_collection = db['portofolios']

def get_portofolio():
    try:
        portofolio = list(portofolio_collection.find({},{'_id':0}))
        return jsonify({"data":portofolio})
    except Exception as e :
        return jsonify({"error" : str(e)}),500
    
def get_portofolio_detail(slug):
    try:
        portofolio_detail=  portofolio_collection.find_one({"slug": slug},{'_id':0})
        return jsonify({"data": portofolio_detail})
    except Exception as e:
        return jsonify({"data" : str(e)})