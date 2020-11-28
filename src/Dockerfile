# Base Image
FROM python:3.8-slim-buster
#FROM python:3.8.0-alpine

# create and set working directory
RUN mkdir /app
WORKDIR /app

# Add current directory code to working directory
ADD . /app/

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# set project environment variables
# grab these via Python's os.environ
# these are 100% optional here
ENV PORT=8888

# Install system dependencies
#RUN apt-get update && apt-get install -y --no-install-recommends \
#        tzdata \
#        python3-setuptools \
#        python3-pip \
#        python3-dev \
#        python3-venv \
#        git \
#        && \
#    apt-get clean && \
#    rm -rf /var/lib/apt/lists/*


# install only the base

RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

# install environment dependencies
RUN pip3 install --upgrade pip

RUN pip3 install pipenv

# Install project dependencies
#RUN pipenv install --skip-lock --system --dev -r requirements.txt
#RUN pip install -r requirements.txt

# Collect static files
RUN python /app/manage.py collectstatic --noinput

RUN python /app/manage.py migrate

EXPOSE 8888

CMD gunicorn djpitime.wsgi:application --bind 0.0.0.0:$PORT


