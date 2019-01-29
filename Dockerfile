FROM ubuntu:latest
MAINTAINER Shoaib Nasir "shoaib.ahmed.nasir@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

# Add source files
COPY Rest_app/ /Rest_app
WORKDIR /Rest_app

# Install requirements
RUN pip install requirements.txt

EXPOSE 5000
COPY entrypoint.sh entrypoint.sh

CMD ["./entrypoint.sh"]