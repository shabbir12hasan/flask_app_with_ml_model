from stringdetector.libs.physical_data_model.connector import DataConnector

from io import BytesIO
import dill as pickle

class AIObject(DataConnector):
    def __init__(self):
        DataConnector.__init__(self)
        self.bucket_name = 'shabbir12hasan'
        self.location = 'test/flask_api_ml_model'
    
    # store pickle in s3
    def _save_to_s3(self, model, filename):
        # self.s3_res.Bucket(self.bucket_name).put_object(
        # Key='{location}/{filename}'.format(location=self.location, filename=filename),
        # Body=model
        # )
        raise NotImplementedError

    # load pickle from s3
    def _load_from_s3(self, filename):
        formula = self.s3.get_object(
            Bucket=self.bucket_name,
            Key='{location}/{filename}'.format(location = self.location, filename = filename)
        )
        return formula['Body']


class ModelDataObject(AIObject):
    def __init__(self):
        AIObject.__init__(self)

    # Save pickle object to s3
    def save_model_object(self, pipeline_bytes, location, bucket, pipeline_type, connector):
    #     self._save_to_s3(pipeline_bytes.read(),location,bucket,filename = '{pipeline_type}.pkl'.format(pipeline_type = pipeline_type), connector=connector)
        raise NotImplementedError


    # Extracting the s3 object, unpickling it and returning the model
    def load_model_object(self, name):
        # name = 'logreg_model.pkl'
        print("Loading {name} from s3".format(name=name))
        body = self._load_from_s3(name)
        bytes = BytesIO(body.read())
        bytes.seek(0)
        return pickle.load(bytes)