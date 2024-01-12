FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder
RUN pip install --upgrade pip
WORKDIR /usr/src/app

COPY requirements.txt .
COPY . .
RUN pip install -r requirements.txt 
ENV SWITCHIPLIST=${SWITCHIPLIST}
ENV USERNAME=${USERNAME}
ENV PASSWORD=${PASSWORD}