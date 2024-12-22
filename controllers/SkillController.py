from flask import Flask, request, jsonify,Blueprint
from pymongo import MongoClient
from dotenv import load_dotenv
from config import DevelopmentConfig, ProductionConfig
from db import db
import os



skill_collection = db['skills']

def get_skill():
    try:
        skill = list(skill_collection.find({},{'_id':0}))
        return jsonify({"data":skill})
    except Exception as e :
        return jsonify({"error" : str(e)}),500
    
    