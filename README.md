## Procedure to run this app locally:
1. Create a virtual env
- python -m venv venv
2. Activate the virutal env
- source venv/bin/activate
3. set flask app with the command
- SET FLASK_APP=test_2.py
4. Then execute flask
- flask run


## Publishing Flask app via docker
### Docker commnad
- Naviagete to apps folder inside devops to run docker commands

1. Remove already existing docker image (if any)
- docker image rm --force stringdetectorml
2. Build a new docker image
- make build-string-detector
3.  Run docker image
- docker run -p 5001:5001 stringdetectorml
4. Investigate the image
- docker run -it stringdetectorml sh
