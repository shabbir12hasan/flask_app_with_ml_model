from stringdetector.libs.physical_data_model.connector import DataConnector
from datetime import datetime

class DataInsert(DataConnector):
    def __init__(self):
        super().__init__()

    def insert_record_in_mongo(self, data):
        rec = {
            'time_created' : datetime.now(),
            'height' : str(data['height']),
            'length' : str(data['length']),
            'result' : str(data['result'])
        }

        if self.flask_api_db is None:
            db = self.con_mongo.TestDB
            self.flask_api_db = db.flask_api

        return self.flask_api_db.insert_one(rec)