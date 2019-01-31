FROM ubuntu:latest
MAINTAINER Shoaib Nasir "shoaib.ahmed.nasir@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

# Add source files
COPY Rest_app/ /Rest_app
COPY requirements.txt /Rest_app
WORKDIR /Rest_app

# Install requirements
RUN pip install -r requirements.txt
RUN ["chmod", "+x", "./entrypoint.sh"]

EXPOSE 5000

ENTRYPOINT ["./entrypoint.sh"]
