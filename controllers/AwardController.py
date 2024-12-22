from flask import Flask, request, jsonify,Blueprint
from pymongo import MongoClient
from dotenv import load_dotenv
from config import DevelopmentConfig, ProductionConfig
from db import db
import os



award_collection = db['awards']

def get_award():
    try:
        award = list(award_collection.find({},{'_id':0}))
        return jsonify({"data":award})
    except Exception as e :
        return jsonify({"error" : str(e)}),500
    
    