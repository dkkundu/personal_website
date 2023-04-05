# pull official base image
FROM python:3.8-slim-buster

# setting work directory
WORKDIR /app

# env variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWEITEBYTECODE 1

# install psycopg dependencies
RUN apt-get update && apt-get install -y libcairo2-dev libpango1.0-dev build-essential libpq-dev python3-pip libpango-1.0-0 libharfbuzz$ && rm -rf /var/lib/apt/lists/*

ENV LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/:$LD_LIBRARY_PATH

# install package
RUN pip install --upgrade pip
RUN pip install django-environ
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install gunicorn

# make work dir
COPY . /app

COPY ./nginx/entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]

