FROM python:3.7-slim-buster

# ARG AWS_ACCOUNT_ID
# ARG AWS_DEFAULT_REGION
ARG APP_ENVIRON

# RUN apt-get update -y && \
#     apt-get install -y python-pip python-dev
####################################################
# copy application and set it up
####################################################
# COPY ./src /opt/src

# ENV PYTHONPATH="$PYTHONPATH:/opt/src/"
# ENV APP_ENVIRON=${APP_ENVIRON}

# RUN pip3 install awscli --upgrade --user
# RUN pip install --trusted-host pypi.python.org -r /opt/src/cinch/apps/mongo_trigger/requirements.txt
# WORKDIR C:/Users/Hasan/Documents/Personal_Git/Flask API/StringDetector_ml/

# copy over our requirements.txt file
COPY ./requirements.txt /tmp/

# WORKDIR /project
# ADD . /project

# upgrade pip and install required python packages
# RUN pip install -U pip
# RUN pip install -r /tmp/requirements.txt

# ENV PYTHONPATH="$PYTHONPATH:/opt/src/"
# ENV APP_ENVIRON=${APP_ENVIRON}
RUN echo 'test'
# RUN echo PYTHONPATH
# Copy application SRC and Binaries
COPY ../../../src /opt/src
# COPY ./src/ app 
WORKDIR /app

EXPOSE 5001

# run mainline
# ENTRYPOINT ["sh", "-c", "python -m Dockerfile"]

CMD [ "python", "app.py", "--host", "0.0.0.0"]