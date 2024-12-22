import os 
from dotenv import load_dotenv


load_dotenv()

class Config:
    MONGO_URI = os.getenv('MONGO_URI')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False