# How to run this app?
1. Activate the virutal env
2. set flask app with the command: SET FLASK_APP=test_2.py
3. Then execute flask: flask run


# naviagete to apps folder inside devops

## remove already existing image
docker image rm --force stringdetectorml

## build a new image
make build-string-detector

## run image
docker run -p 5001:5001 stringdetectorml

## investigate the image
docker run -it stringdetectorml sh