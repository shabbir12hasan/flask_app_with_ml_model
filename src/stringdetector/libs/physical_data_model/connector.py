import json
import boto3

class DataConnector():
    def __init__(self):
        with open("credentials.json", 'rb') as f:
            self.creds = json.load(f)
            
        self.create_s3_connection()

        
        
    

    def create_s3_connection(self):
        self.s3 = boto3.client('s3', aws_access_key_id=self.creds['aws']['key'],
         aws_secret_access_key= self.creds['aws']['secret'])
        self.s3_res = boto3.resource('s3', aws_access_key_id=self.creds['aws']['key'],
         aws_secret_access_key= self.creds['aws']['secret'])