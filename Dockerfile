FROM python:3.11
WORKDIR /home/usr/app
COPY . .
RUN apt-get -y install curl
RUN pip install -r requirements.txt