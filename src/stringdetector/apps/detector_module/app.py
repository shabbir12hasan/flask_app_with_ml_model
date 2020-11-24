from detector_app import StringDetector
from flask import Flask, render_template
from flask import request


app = Flask(__name__)
main_app = StringDetector()

# load the pipeline object
from io import BytesIO
import dill as pickle
model_path = 'stringdetector/apps/bin/logreg_model.pkl' # for running in docker
# model_pathcd  = '../bin/logreg_model.pkl' # for running locally
log_reg = open(model_path ,'rb')
model = pickle.load(log_reg)
# model.predict([[3,4]])


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


    # print("*****", req_data['id'])
    # print("*****", req_data['input_message'])
    
    output = model.predict([[inp_length, inp_height]])
    ret_message = 'Mesage ID:{id} \n Length:{inp_length} \n Height:{inp_height} \n Model output widht:{output}'.format(
        id='Test'
        ,inp_length=inp_length
        ,inp_height=inp_height
        ,output=output
    )
    return ret_message


if __name__=="__main__":
    app.run(host ='0.0.0.0', port = 5001)
