FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt -y update
RUN apt -y install python3 python3-pip
RUN pip install Flask

RUN mkdir /service
COPY hello-service.py /service/hello-service.py

EXPOSE 5000

CMD ["python3", "/service/hello-service.py"]