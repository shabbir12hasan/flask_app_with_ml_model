### Update 1.0.0
- Taking the ML model from AWS s3 bucket
- Storing the processed data and results on MongoDB hosted on AWS EC2

### Introduction:
This project is demonstrating how we can integrate a Machine Learning(ML) model with a Python Flask application and generate an API. This code extract the model from AWS S3 and store the model outputs in MongoDB living on AWS EC2.

#### Problem
Incoming users on the website should see intelligent search results on the live website. 
<p align="center"><img src="https://github.com/shabbir12hasan/flask_app_with_ml_model/blob/master/app_architecture/user_website_interactin.png" width="850"/></p>

#### Solution
Building a Flask API which will allow user to insert the data and get results from ML model.
<p align="center"><img src="https://github.com/shabbir12hasan/flask_app_with_ml_model/blob/master/app_architecture/Flask_app.png" width="850"/></p>


### Requirements:
- Python 3.7
- Docker installed and set up (Docker has a very detailed documentation, https://docs.docker.com/engine/install/ubuntu/)
- Virtual env with all project libraries installed
- AWS account with S3 and MongoDB
- Credential file with AWS creds
- Model stored in s3

### Setup:
1. Create a virtual env
- python -m venv venv
2. Activate the virutal env
- source venv/bin/activate
3. Install project libraries
- pip install -r requirements.txt
4. set flask app with the command
- SET FLASK_APP=test_2.py
5. Then execute flask
- flask run


### Dockerizing Flask app:
#### Docker commands
- Navigate to apps folder inside DevOps to run docker commands

1. Remove already existing docker image (if any)
- docker image rm --force stringdetectorml
2. Build a new docker image
- make build-string-detector
3.  Run docker image
- docker run -p 5001:5001 stringdetectorml
4. Investigate the image
- docker run -it stringdetectorml sh
