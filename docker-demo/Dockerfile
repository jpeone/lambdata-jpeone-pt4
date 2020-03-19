FROM debian

### So logging/io works reliably w/Docker
ENV PYTHONUNBUFFERED=1
### UTF Python issue for Click package (pipenv dependency)
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
### Need to explicitly set this so `pipenv shell` works
ENV SHELL=/bin/bash

### Basic Python dev dependencies
RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install python3-pip curl -y && \
  pip3 install pipenv && \
  # this seems counter intuitive to all the work we've been doing
  # creating these environments, but I can't get a damn pipenv to
  # work in this container for the life of me
  pip3 install numpy && \
  pip3 install scikit-learn &&\
  pip3 install pandas &&\ 
  pip3 install -i https://test.pypi.org/simple/ lambdata-jpeone-pt4