# How to run this app?
1. Activate the virutal env
2. set flask app with the command: SET FLASK_APP=test_2.py
3. Then execute flask: flask run


### Docker tips:
### Naviagete to apps folder inside devops to run docker commands

### Remove already existing docker image
docker image rm --force stringdetectorml

### Build a new docker image
make build-string-detector

### Run docker image
docker run -p 5001:5001 stringdetectorml

### Investigate the image
docker run -it stringdetectorml sh
