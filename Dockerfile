FROM python:3.9-slim
LABEL maintainer="kovalisko.veronika@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR spend_tracker/

COPY requirements.txt .

RUN apt-get update  \
    && apt-get -y install libpq-dev gcc

RUN pip install -r requirements.txt

COPY . .


RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user


USER django-user
