from flask import Flask, request, jsonify,Blueprint
from pymongo import MongoClient
from dotenv import load_dotenv
from config import DevelopmentConfig, ProductionConfig
from db import db
from bson import ObjectId
import os



award_collection = db['awards']
award_image_collection = db['awardimages']


def get_award():
    try:
        award = list(award_collection.find({}))
        for i in range(len(award)):
            award[i]['_id'] = str(award[i]['_id'])
        return jsonify({"data":award})
    except Exception as e :
        return jsonify({"error" : str(e)}),500
    
def get_award_detail(slug):
    try:
        award_detail = award_collection.find_one({"slug": slug})
        if award_detail and isinstance(award_detail, dict):
            award_detail['_id'] = str(award_detail['_id'])

        return jsonify({"data":award_detail})
    except Exception as e:
        return jsonify({"error": str(e)}),500
    

def get_award_list(oid):
    try:
        awardid = ObjectId(oid)
        award_list = list(award_image_collection.find({"awardid": awardid}, {'_id': 0, 'awardid': 0}))
        award_list.sort(key=lambda x: x.get('sort', ''))

        for award in award_list:
            if 'awardid' in award:
                award['awardid'] = str(award['awardid'])
        return jsonify({"data": award_list}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def get_award_image():
    try:
        awardImage = list(award_image_collection.find({}))

        for i in range(len(awardImage)):
            awardImage[i]['_id'] = str(awardImage[i]['_id'])

        for award in awardImage:
            if 'awardid' in award:
                award['awardid'] = str(award['awardid'])
        return jsonify({"data":awardImage})
    except Exception as e :
        return jsonify({"error" : str(e)}),500
    