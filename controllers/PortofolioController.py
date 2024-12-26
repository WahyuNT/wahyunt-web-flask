from flask import Flask, request, jsonify,Blueprint
from pymongo import MongoClient
from dotenv import load_dotenv
from config import DevelopmentConfig, ProductionConfig
from db import db
from bson import ObjectId
import os

portofolio_collection = db['portofolios']
portofolio_image_collection = db['imageportofolios']


def get_portofolio():
    keyword = request.args.get('keyword', '')
    try:
        if keyword:
            portfolio = list(portofolio_collection.find(
                {"type": {"$regex": keyword, "$options": "i"}},
                {"_id": 0}
            ))
        else:
            portfolio = list(portofolio_collection.find({}, {"_id": 0}))
        return jsonify({"data": portfolio})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
def get_portofolio_detail(slug):
    try:
        portofolio_detail=  portofolio_collection.find_one({"slug": slug})

        if portofolio_detail and isinstance(portofolio_detail, dict):
            portofolio_detail['_id'] = str(portofolio_detail['_id'])
        return jsonify({"data": portofolio_detail})
    except Exception as e:
        return jsonify({"data" : str(e)})
    
def get_portofolio_list(oid):
    try:
        portofolio = ObjectId(oid)

        portofolio_list = list(portofolio_image_collection.find({"portofolio": portofolio}, {'_id': 0, 'portofolio': 0}))
        portofolio_list.sort(key=lambda x: x.get('sort', ''))

        for portofolio in portofolio_list:
            if 'portofolio' in portofolio:
                portofolio['portofolio'] = str(portofolio['portofolio'])
        return jsonify({"data": portofolio_list}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500