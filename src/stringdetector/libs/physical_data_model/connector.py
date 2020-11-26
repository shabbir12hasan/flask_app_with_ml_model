import json
import boto3
from pymongo import MongoClient

class DataConnector():
    def __init__(self):
        with open("src/stringdetector/apps/detector_module/credentials.json", 'rb') as f:
        # with open("credentials.json", 'rb') as f:
            self.creds = json.load(f)

        self.create_s3_connection()
        self.create_mongo_connection()
        # MongoDB database
        self.flask_api_db = None


    def create_s3_connection(self):
        self.s3 = boto3.client('s3', aws_access_key_id=self.creds['aws']['key'],
         aws_secret_access_key= self.creds['aws']['secret'])
        self.s3_res = boto3.resource('s3', aws_access_key_id=self.creds['aws']['key'],
         aws_secret_access_key= self.creds['aws']['secret'])


    def create_mongo_connection(self):
        self.con_mongo = MongoClient(
            self.creds['mongo']['server'],
            username=self.creds['mongo']['user'],
            password=self.creds['mongo']['pass']
        )