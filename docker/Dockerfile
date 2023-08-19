FROM python:3.9
#
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install -y make
RUN apt install -y libsm6 libxext6 libkeyutils-dev gcc
RUN apt install -y build-essential

COPY . /app
WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 9090
CMD python3 /app/backend-chatbot/manage.py runserver
