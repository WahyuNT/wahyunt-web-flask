from pymongo import MongoClient
from config import DevelopmentConfig, ProductionConfig
import os

if os.getenv('FLASK_ENV') == 'production':
    active_config = ProductionConfig
else:
    active_config = DevelopmentConfig


client= MongoClient(active_config.MONGO_URI)
db = client['web_wahyunt']