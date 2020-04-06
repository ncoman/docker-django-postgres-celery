# pull official base image
FROM python:3.7.7
MAINTAINER Nick <koleas@gmail.com>

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV APP_HOME=/home/app/web

# create the appropriate directories
RUN mkdir -p $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles

# Setup Celery
#RUN adduser -D -H celery \
#  && mkdir -p /var/run/celery \
#  && chown celery:celery /var/run/celery

# set work directory
WORKDIR $APP_HOME

# install dependencies on Production
RUN apt-get update
RUN apt-get install -y --no-install-recommends\
    git \
    vim

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements/default.txt $APP_HOME/default.txt
RUN pip install -r default.txt

# copy project
COPY . $APP_HOME

# Entrypoint
COPY ./entrypoint.sh $APP_HOME/entrypoint.sh
RUN chmod +x /home/app/web/entrypoint.sh
RUN /home/app/web/entrypoint.sh
RUN echo "Complete"
