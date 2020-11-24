import boto3
from io import BytesIO
import dill as pickle

bucket_name='shabbir12hasan'

s3 = boto3.client('s3')
s3_resource = boto3.resource('s3')

formula = s3.get_object(
        Bucket=bucket_name,
        Key='{location}/{filename}'.format(location = "test/flask_api_ml_model", filename = "logreg_model.pkl")
    )
body = formula['Body']
bytes = BytesIO(body.read())
bytes.seek(0)
log_reg = pickle.load(bytes)


## functions to be implemented
def _save_to_s3(stuff, location, bucket, filename, connector):
    connector.s3_res.Bucket(bucket).put_object(
    Key='{location}/{filename}'.format(location=location, filename=filename),
    Body=stuff
    )

def _load_from_s3(location, bucket, filename, connector):
    formula = connector.s3.get_object(
        Bucket=bucket,
        Key='{location}/{filename}'.format(location = location, filename = filename)
    )
    return formula['Body']
    