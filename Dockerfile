FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

RUN apk --update add bash nano
RUN mkdir app
COPY ./app/ /app/app/
COPY ./app/uwsgi.ini .
ENV STATIC_PATH /app/app/static
COPY ./requirements.txt .
RUN pip install -r requirements.txt