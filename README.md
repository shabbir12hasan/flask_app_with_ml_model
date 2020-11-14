### Introduction:
This project is demonstrating how we can integrate a Machine Learning(ML) model with a Python Flask application and then deploy the whole application using dockers.


### Requirements:
- Python 3.7
- Docker installed and set up (Docker has a very detailed documentation, https://docs.docker.com/engine/install/ubuntu/)
- Virtual env with all project libraries installed

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
