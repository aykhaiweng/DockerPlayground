FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /opt/webapp/
COPY . /opt/webapp/
WORKDIR /opt/webapp/
RUN pip install -U pip
RUN pip install -r requirements.txt
