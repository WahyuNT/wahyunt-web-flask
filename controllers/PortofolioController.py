from flask import Flask, request, jsonify,Blueprint
from pymongo import MongoClient
from dotenv import load_dotenv
from config import DevelopmentConfig, ProductionConfig
from db import db
from bson import ObjectId
import os
import json

portofolio_collection = db['portofolios']
portofolio_image_collection = db['imageportofolios']


def get_portofolio():
    keyword = request.args.get('keyword', '')
    try:
        # Sesuaikan path untuk naik satu level ke atas dari controllers
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)  # Naik satu level ke atas
        json_path = os.path.join(parent_dir, 'lib', 'portofolio.json')
        
        with open(json_path, 'r', encoding='utf-8') as file:
            portfolio = json.load(file)
            
        # Filter berdasarkan keyword jika ada
        if keyword:
            filtered_portfolio = [
                item for item in portfolio 
                if keyword.lower() in item.get('type', '').lower()
            ]
            return jsonify({"data": filtered_portfolio})
            
        return jsonify({"data": portfolio})
    
    except FileNotFoundError:
        return jsonify({"error": "File portofolio.json tidak ditemukan"}), 404
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