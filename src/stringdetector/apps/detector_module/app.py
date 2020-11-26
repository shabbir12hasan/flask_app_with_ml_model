from flask import Flask, render_template
from flask import request

## running locally
# path fix, add to pythonpath or apped the src path here
import sys
# print(sys.path)
sys.path.append("/home/shabbir/Documents/Repo/flask_app_with_ml_model/src/")

from stringdetector.libs.physical_data_model.data_inserts import DataInsert
from stringdetector.libs.ml_models.ai_object import ModelDataObject
from stringdetector.apps.detector_module.detector_app import StringDetector


################ loading model from s3 ###############
model_object = ModelDataObject()
model = model_object.load_model_object(name="logreg_model.pkl")
#######################################################

# Initiating the flask app
app = Flask(__name__)
main_app = StringDetector()


################## loading model from the bin file ###############
# load the pipeline object
# from io import BytesIO
# import dill as pickle
# model_path = 'stringdetector/apps/bin/test_logreg_model.pkl' # for running in docker
# # model_path  = '../bin/logreg_model.pkl' # for running locally
# log_reg = open(model_path ,'rb')
# model = pickle.load(log_reg)
# model.predict([[3,4]])
###################################################################


@app.route('/')
def main():
    return render_template('home_page.html')


@app.route('/tasks', methods=['POST'])
def create_task():
    req_data = request.get_json()
    
    if req_data is None:
        # req_data = request.form
        inp_length = int(request.form['length'])
        inp_height = int(request.form['height'])
    else:
        inp_length = req_data['length']
        inp_height = req_data['height']

    output = model.predict([[inp_length, inp_height]])
    
    # Inserting data in the DB
    data_insert = DataInsert()
    data_insert.insert_record_in_mongo({'height':inp_height, 'length':inp_length, 'result':output[0]})

    ret_message = 'Mesage ID:{id} \n Length:{inp_length} \n Height:{inp_height} \n Model output widht:{output}'.format(
        id='Test'
        ,inp_length=inp_length
        ,inp_height=inp_height
        ,output=output
    )
    return ret_message


if __name__=="__main__":
    app.run(host ='0.0.0.0', port = 5001)