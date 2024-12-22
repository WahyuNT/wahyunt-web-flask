from flask import Flask, request, jsonify,Blueprint
from pymongo import MongoClient
from dotenv import load_dotenv
from config import DevelopmentConfig, ProductionConfig
from db import db
import os



doing_collection = db['doings']

def get_doing():
    try:
        doing = list(doing_collection.find({},{'_id':0}))
        return jsonify({"data":doing})
    except Exception as e :
        return jsonify({"error" : str(e)}),500
    
    